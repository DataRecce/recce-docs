"""Publish a .md mirror for every page and a sitemap.md index.

Lets agents fetch the raw markdown for any docs page by appending `.md` to the
URL (for example `/getting-started/oss-setup.md`), and discover every page from
a single `sitemap.md`.
"""
from __future__ import annotations

import logging
import shutil
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import event_priority
from mkdocs.structure.files import Files

log = logging.getLogger("mkdocs")

_FILES: Files | None = None


def on_files(files: Files, config: MkDocsConfig) -> Files:
    global _FILES
    _FILES = files
    return files


def _mirror_rel(url: str) -> str:
    # MkDocs gives the home page url as '.' or '' depending on plugin chain.
    if not url or url in (".", "./"):
        return "index.md"
    trimmed = url.rstrip("/")
    return f"{trimmed}.md"


def _first_h1(path: Path) -> str | None:
    try:
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                stripped = line.strip()
                if stripped.startswith("# "):
                    return stripped[2:].strip()
    except OSError:
        return None
    return None


@event_priority(-90)
def on_post_build(config: MkDocsConfig) -> None:
    if _FILES is None:
        log.warning("build_md_mirrors: on_files never ran, skipping")
        return
    site_dir = Path(config["site_dir"])
    site_url = (config.get("site_url") or "").rstrip("/")

    entries: list[tuple[str, str]] = []
    written = 0

    for f in _FILES:
        if not f.is_documentation_page():
            continue
        if not f.abs_src_path:
            continue
        src = Path(f.abs_src_path)
        if not src.exists():
            continue
        mirror_rel = _mirror_rel(f.url)
        mirror_abs = site_dir / mirror_rel
        mirror_abs.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, mirror_abs)
        written += 1
        title = _first_h1(src) or (f.url.rstrip("/").split("/")[-1] if f.url else "Home")
        entries.append((title, f"{site_url}/{mirror_rel}"))

    entries.sort(key=lambda e: e[1])

    lines = [
        "# Recce Docs sitemap",
        "",
        "Machine-readable index of every page on docs.reccehq.com. Each link points to the markdown mirror.",
        "",
    ]
    for title, url in entries:
        lines.append(f"- [{title}]({url})")
    (site_dir / "sitemap.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    log.info("build_md_mirrors: wrote %d .md mirrors and sitemap.md", written)
