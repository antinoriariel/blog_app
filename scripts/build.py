#!/usr/bin/env python3
"""
Punto de entrada del generador estático.
Uso: python scripts/build.py
"""
import sys
from pathlib import Path

# Ensure scripts/ is in the path so sibling imports work
sys.path.insert(0, str(Path(__file__).parent))

import shutil

from config import load_config
from utils import scan_posts, parse_entry, validate_frontmatter, copy_assets, write_file
from render import (
    render_post,
    render_index,
    render_tag,
    render_archive,
    render_page,
    render_404,
    render_sitemap,
)
from utils import group_by_tag


def build():
    cfg = load_config()
    base_dir = Path(__file__).parent.parent

    content_dir = base_dir / cfg["build"]["content_dir"]
    output_dir = base_dir / cfg["build"]["output_dir"]
    assets_dir = base_dir / cfg["build"]["assets_dir"]
    templates_dir = base_dir / cfg["build"]["templates_dir"]

    print(f"Limpiando salida anterior en {output_dir} ...")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    copy_assets(assets_dir, output_dir / "assets")

    posts, errors = _load_entries(content_dir / "posts")
    posts.sort(key=lambda p: p["meta"]["date"], reverse=True)

    pages, page_errors = _load_entries(content_dir / "pages", is_page=True)
    errors.extend(page_errors)

    if errors:
        print("\nErrores de validacion:")
        for e in errors:
            print(f"  [ERR] {e}")

    _render_posts(posts, pages, cfg, templates_dir, output_dir)
    _render_pages(pages, posts, cfg, templates_dir, output_dir)

    html = render_index(posts, pages, cfg, templates_dir)
    write_file(output_dir / "index.html", html)

    if cfg["features"].get("tags"):
        _render_tags(posts, pages, cfg, templates_dir, output_dir)

    if cfg["features"].get("archive"):
        html = render_archive(posts, pages, cfg, templates_dir)
        write_file(output_dir / "archivo" / "index.html", html)

    if cfg["features"].get("page_404"):
        html = render_404(posts, pages, cfg, templates_dir)
        write_file(output_dir / "404.html", html)

    if cfg["features"].get("sitemap"):
        write_file(output_dir / "sitemap.xml", render_sitemap(posts, pages, cfg))
        robots = f"Sitemap: {cfg['site']['url'].rstrip('/')}/sitemap.xml\nUser-agent: *\nAllow: /\n"
        write_file(output_dir / "robots.txt", robots)

    print(f"\n[OK] Build completado")
    print(f"  {len(posts)} entrada(s), {len(pages)} pagina(s)")
    print(f"  Salida: {output_dir}")

    if errors:
        print(f"\n[WARN] {len(errors)} error(es) encontrado(s). Revisar arriba.")
        sys.exit(1)


def _load_entries(directory, is_page=False):
    from utils import REQUIRED_FIELDS_PAGE, REQUIRED_FIELDS_POST
    required = REQUIRED_FIELDS_PAGE if is_page else REQUIRED_FIELDS_POST
    entries, errors = [], []
    for path in scan_posts(directory):
        try:
            entry = parse_entry(path)
            validate_frontmatter(entry["meta"], path, required=required)
            if entry["meta"].get("published", True):
                entries.append(entry)
        except Exception as exc:
            errors.append(str(exc))
    return entries, errors


def _render_posts(posts, pages, cfg, templates_dir, output_dir):
    for post in posts:
        html = render_post(post, posts, pages, cfg, templates_dir)
        slug = post["meta"]["slug"]
        write_file(output_dir / "posts" / slug / "index.html", html)


def _render_pages(pages, posts, cfg, templates_dir, output_dir):
    for page in pages:
        html = render_page(page, posts, pages, cfg, templates_dir)
        slug = page["meta"]["slug"]
        write_file(output_dir / slug / "index.html", html)


def _render_tags(posts, pages, cfg, templates_dir, output_dir):
    by_tag = group_by_tag(posts)
    for tag, tag_posts in by_tag.items():
        from utils import slugify
        html = render_tag(tag, tag_posts, posts, pages, cfg, templates_dir)
        write_file(output_dir / "etiquetas" / slugify(tag) / "index.html", html)
    # Tags index (tag=None shows all tags)
    html = render_tag(None, [], posts, pages, cfg, templates_dir, all_tags=by_tag)
    write_file(output_dir / "etiquetas" / "index.html", html)


if __name__ == "__main__":
    build()
