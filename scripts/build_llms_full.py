"""Concatenate all rendered docs into site/llms-full.txt."""
from __future__ import annotations

import re
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import event_priority


@event_priority(-100)
def on_post_build(config: MkDocsConfig) -> None:
    site = Path(config["site_dir"])
    sitemap_path = site / "sitemap.xml"
    if not sitemap_path.exists():
        return
    sitemap = sitemap_path.read_text(encoding="utf-8")
    urls = sorted(set(re.findall(r"<loc>(.*?)</loc>", sitemap)))
    parts: list[str] = ["# Recce Documentation — Full Corpus\n"]
    for url in urls:
        rel = url.rsplit("docs.reccehq.com/", 1)[-1].rstrip("/")
        html_path = site / rel / "index.html" if rel else site / "index.html"
        if not html_path.exists():
            continue
        html = html_path.read_text(encoding="utf-8")
        main = re.search(r"<main[^>]*>(.*?)</main>", html, re.DOTALL)
        if not main:
            continue
        body = main.group(1)
        # Strip script/style blocks before tag-stripping to avoid CSS/JS leakage.
        body = re.sub(r"<script[^>]*>.*?</script>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r"<style[^>]*>.*?</style>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r"<noscript[^>]*>.*?</noscript>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        # Strip HTML comments.
        body = re.sub(r"<!--.*?-->", " ", body, flags=re.DOTALL)
        # Strip remaining tags.
        text = re.sub(r"<[^>]+>", " ", body)
        # Decode common HTML entities.
        text = (
            text.replace("&nbsp;", " ")
            .replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&quot;", '"')
            .replace("&#39;", "'")
        )
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        parts.append(f"\n\n---\n## {url}\n\n{text}")
    (site / "llms-full.txt").write_text("\n".join(parts), encoding="utf-8")
