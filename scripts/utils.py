import re
import shutil
import unicodedata
from pathlib import Path
from datetime import date, datetime

import yaml
import markdown as md_lib

REQUIRED_FIELDS_POST  = ["title", "slug", "date", "summary"]
REQUIRED_FIELDS_PAGE  = ["title", "slug"]
REQUIRED_FIELDS       = REQUIRED_FIELDS_POST  # default; callers can override

_MD_EXTENSIONS = ["tables", "fenced_code", "toc", "attr_list", "footnotes", "nl2br"]

# Matches the opening --- and closing --- of a YAML frontmatter block.
# Handles trailing spaces after the dashes and both LF/CRLF line endings.
_FRONTMATTER_RE = re.compile(r'\A---[ \t]*\n(.*?)\n---[ \t]*\n?(.*)', re.DOTALL)

# Display math: $$...$$  (multiline content allowed)
_MATH_DISPLAY_RE = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)
# Inline math: $...$ — no spaces at boundaries, no newlines inside, not preceded/followed by $
_MATH_INLINE_RE = re.compile(r'(?<!\$)\$(?!\s)([^\$\n]+?)(?<!\s)\$(?!\$)')


def _protect_math(text):
    """Extract LaTeX blocks before Markdown processing to prevent symbol mangling.

    Markdown interprets _ * < > as formatting; without protection, LaTeX like
    x_{i} or a < b inside $...$ gets corrupted. This function replaces each
    math block with an opaque placeholder and returns the mapping so
    _restore_math() can re-insert the rendered HTML afterwards.

    Display blocks ($$...$$) are surrounded by blank lines so that Markdown
    wraps the placeholder in a <p>, which _restore_math() then removes.
    """
    slots = []  # list of ('display'|'inline', raw_latex_content)

    def save_display(m):
        idx = len(slots)
        slots.append(('display', m.group(1)))
        return f'\n\nMATHPH{idx}D\n\n'

    def save_inline(m):
        idx = len(slots)
        slots.append(('inline', m.group(1)))
        return f'MATHPH{idx}I'

    text = _MATH_DISPLAY_RE.sub(save_display, text)
    text = _MATH_INLINE_RE.sub(save_inline, text)
    return text, slots


def _restore_math(html, slots):
    """Replace placeholders left by _protect_math() with KaTeX-ready HTML.

    Display math → <div class="math-display">\\[...\\]</div>
    Inline math  → <span class="math-inline">\\(...\\)</span>

    The \\[...\\] and \\(...\\) delimiter pairs are the standard KaTeX
    auto-render delimiters configured in the post template.
    """
    for idx, (kind, content) in enumerate(slots):
        if kind == 'display':
            block = f'<div class="math-display">\\[{content}\\]</div>'
            # Markdown wraps the block-level placeholder in <p>; strip that wrapper.
            # Use a lambda so re.sub does not interpret backslashes in `block`.
            html = re.sub(rf'<p>\s*MATHPH{idx}D\s*</p>', lambda _: block, html)
        else:
            span = f'<span class="math-inline">\\({content}\\)</span>'
            html = html.replace(f'MATHPH{idx}I', span)
    return html


def slugify(text):
    text = str(text).lower().strip()
    # Decompose unicode (á → a + combining accent) then drop non-ASCII
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text)


def scan_posts(directory):
    directory = Path(directory)
    if not directory.exists():
        return []
    return sorted(directory.glob("*.md"))


def parse_entry(path):
    # utf-8-sig strips the UTF-8 BOM automatically if present
    text = Path(path).read_text(encoding="utf-8-sig")
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    m = _FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError(
            f"Frontmatter inválido en {Path(path).name}: el archivo debe empezar con ---"
        )

    meta = yaml.safe_load(m.group(1))
    if not isinstance(meta, dict):
        raise ValueError(f"El frontmatter no es un diccionario YAML válido en {Path(path).name}")

    body = m.group(2).strip()

    # Normalize date to a date object
    if "date" in meta:
        raw = meta["date"]
        if isinstance(raw, date):
            meta["date"] = raw
        else:
            meta["date"] = datetime.strptime(str(raw), "%Y-%m-%d").date()

    body_protected, math_slots = _protect_math(body)
    body_html = md_lib.markdown(body_protected, extensions=_MD_EXTENSIONS)
    body_html = _restore_math(body_html, math_slots)

    return {"meta": meta, "body": body, "body_html": body_html, "path": path, "use_math": bool(math_slots)}


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
