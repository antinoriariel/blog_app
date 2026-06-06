from pathlib import Path
from datetime import date, datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from utils import group_by_tag, group_by_month, slugify


def _make_env(templates_dir, cfg):
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html"]),
    )

    def format_date(d, fmt="%d %b %Y"):
        if isinstance(d, (date, datetime)):
            return d.strftime(fmt)
        return str(d)

    env.filters["date"] = format_date
    env.filters["slugify"] = slugify
    env.globals["site"] = cfg["site"]
    env.globals["base_url"] = cfg["build"].get("base_url", "/")
    env.globals["features"] = cfg.get("features", {})

    return env


def render_post(post, all_posts, pages, cfg, templates_dir):
    env = _make_env(templates_dir, cfg)
    tmpl = env.get_template("post.html")

    idx = all_posts.index(post)
    prev_post = all_posts[idx + 1] if idx + 1 < len(all_posts) else None
    next_post = all_posts[idx - 1] if idx > 0 else None

    return tmpl.render(
        post=post,
        pages=pages,
        prev_post=prev_post,
        next_post=next_post,
        all_tags=group_by_tag(all_posts),
    )


def render_index(posts, pages, cfg, templates_dir):
    env = _make_env(templates_dir, cfg)
    tmpl = env.get_template("index.html")

    featured = [p for p in posts if p["meta"].get("featured")]
    recent = posts[: cfg["build"].get("posts_per_page", 10)]

    return tmpl.render(
        posts=recent,
        featured=featured,
        pages=pages,
        all_tags=group_by_tag(posts),
    )


def render_tag(tag, tag_posts, all_posts, pages, cfg, templates_dir, all_tags=None):
    env = _make_env(templates_dir, cfg)
    tmpl = env.get_template("tag.html")

    return tmpl.render(
        tag=tag,
        posts=tag_posts,
        pages=pages,
        all_tags=all_tags or group_by_tag(all_posts),
    )


def render_archive(posts, pages, cfg, templates_dir):
    env = _make_env(templates_dir, cfg)
    tmpl = env.get_template("archive.html")

    return tmpl.render(
        posts=posts,
        pages=pages,
        by_month=group_by_month(posts),
        all_tags=group_by_tag(posts),
    )


def render_page(page, all_posts, pages, cfg, templates_dir):
    env = _make_env(templates_dir, cfg)
    tmpl = env.get_template("page.html")

    return tmpl.render(
        page=page,
        pages=pages,
        all_tags=group_by_tag(all_posts),
    )


def render_404(all_posts, pages, cfg, templates_dir):
    env = _make_env(templates_dir, cfg)
    tmpl = env.get_template("404.html")

    return tmpl.render(
        posts=all_posts[:5],
        pages=pages,
        all_tags=group_by_tag(all_posts),
    )


def render_sitemap(posts, pages, cfg):
    base = cfg["site"]["url"].rstrip("/")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        f"  <url><loc>{base}/</loc></url>",
    ]
    for post in posts:
        slug = post["meta"]["slug"]
        d = post["meta"]["date"]
        lines.append(f"  <url><loc>{base}/posts/{slug}/</loc><lastmod>{d}</lastmod></url>")
    for page in pages:
        slug = page["meta"]["slug"]
        lines.append(f"  <url><loc>{base}/{slug}/</loc></url>")
    lines.append("</urlset>")
    return "\n".join(lines)
