import re
import shutil
from pathlib import Path
from datetime import date, datetime

import yaml
import markdown as md_lib

REQUIRED_FIELDS_POST  = ["title", "slug", "date", "summary"]
REQUIRED_FIELDS_PAGE  = ["title", "slug"]
REQUIRED_FIELDS       = REQUIRED_FIELDS_POST  # default; callers can override

_MD_EXTENSIONS = ["tables", "fenced_code", "toc", "attr_list", "footnotes", "nl2br"]


def slugify(text):
    text = str(text).lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text)


def scan_posts(directory):
    directory = Path(directory)
    if not directory.exists():
        return []
    return sorted(directory.glob("*.md"))


def parse_entry(path):
    text = Path(path).read_text(encoding="utf-8")

    if not text.startswith("---"):
        raise ValueError("El archivo no tiene bloque frontmatter inicial")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Frontmatter malformado: falta el cierre '---'")

    meta = yaml.safe_load(parts[1])
    if not isinstance(meta, dict):
        raise ValueError("El frontmatter no es un diccionario YAML válido")

    body = parts[2].strip()

    # Normalize date to a date object
    if "date" in meta:
        raw = meta["date"]
        if isinstance(raw, date):
            meta["date"] = raw
        else:
            meta["date"] = datetime.strptime(str(raw), "%Y-%m-%d").date()

    body_html = md_lib.markdown(body, extensions=_MD_EXTENSIONS)

    return {"meta": meta, "body": body, "body_html": body_html, "path": path}


def validate_frontmatter(meta, path, required=None):
    if required is None:
        required = REQUIRED_FIELDS_POST
    for field in required:
        if not meta.get(field):
            raise ValueError(f"Campo obligatorio '{field}' faltante o vacio en {Path(path).name}")

    slug = str(meta.get("slug", ""))
    if not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", slug):
        raise ValueError(
            f"Slug inválido '{slug}' en {Path(path).name}: solo minúsculas, números y guiones"
        )

    if "date" in required and not isinstance(meta.get("date"), date):
        raise ValueError(f"Fecha invalida en {Path(path).name}: debe ser formato YYYY-MM-DD")


def group_by_tag(posts):
    tags = {}
    for post in posts:
        for tag in post["meta"].get("tags") or []:
            tags.setdefault(tag, []).append(post)
    return dict(sorted(tags.items()))


def group_by_month(posts):
    months = {}
    for post in posts:
        key = post["meta"]["date"].strftime("%Y-%m")
        label = post["meta"]["date"].strftime("%B %Y").capitalize()
        months.setdefault(key, {"label": label, "posts": []})["posts"].append(post)
    return dict(sorted(months.items(), reverse=True))


def copy_assets(src, dst):
    src, dst = Path(src), Path(dst)
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)


def write_file(path, content):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
