"""Concatenate all rendered docs into site/llms-full.txt."""
from __future__ import annotations

import html
import logging
import re
from pathlib import Path
from urllib.parse import urlparse

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import event_priority

EXPECTED_HOST = "docs.reccehq.com"

log = logging.getLogger("mkdocs")


@event_priority(-100)
def on_post_build(config: MkDocsConfig) -> None:
    site = Path(config["site_dir"])
    sitemap_path = site / "sitemap.xml"
    if not sitemap_path.exists():
        log.warning("build_llms_full: %s not found, skipping llms-full.txt", sitemap_path)
        return
    sitemap = sitemap_path.read_text(encoding="utf-8")
    urls = sorted(set(re.findall(r"<loc>(.*?)</loc>", sitemap)))
    parts: list[str] = ["# Recce Documentation — Full Corpus\n"]
    for url in urls:
        parsed = urlparse(url)
        if parsed.netloc and parsed.netloc != EXPECTED_HOST:
            continue
        rel = parsed.path.strip("/")
        html_path = site / rel / "index.html" if rel else site / "index.html"
        if not html_path.exists():
            log.warning("build_llms_full: missing %s for sitemap URL %s", html_path, url)
            continue
        page_html = html_path.read_text(encoding="utf-8")
        # Material puts nav and TOC sidebars inside <main>, so selecting <main>
        # would duplicate the entire nav tree into every section. The actual
        # page content lives in <article class="md-content__inner">.
        article = re.search(
            r'<article[^>]*class="[^"]*md-content__inner[^"]*"[^>]*>(.*?)</article>',
            page_html,
            re.DOTALL,
        )
        if not article:
            log.warning("build_llms_full: no md-content__inner article in %s", html_path)
            continue
        body = article.group(1)
        # Strip script/style blocks before tag-stripping to avoid CSS/JS leakage.
        body = re.sub(r"<script[^>]*>.*?</script>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r"<style[^>]*>.*?</style>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r"<noscript[^>]*>.*?</noscript>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r"<!--.*?-->", " ", body, flags=re.DOTALL)
        text = re.sub(r"<[^>]+>", " ", body)
        text = html.unescape(text)
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        parts.append(f"\n\n---\n## {url}\n\n{text}")
    (site / "llms-full.txt").write_text("\n".join(parts), encoding="utf-8")
