from pathlib import Path
from pelican import signals
from bs4 import BeautifulSoup

# Temporarily store pages and their source paths
all_pages = []


def collect_pages(generator):
    """Collect all Page objects after generation."""
    all_pages.extend(generator.pages)
    all_pages.extend(generator.hidden_pages)


def extract_top_toc(pages):
    """Extract the top-level table of contents from the pages."""
    for page in pages:
        toc_html = getattr(page, "toc", None)
        if not toc_html:
            continue

        soup = BeautifulSoup(toc_html, "html.parser")
        sections = []

        # Typically, the outermost UL contains the top-level TOC entries
        top_ul = soup.find("ul")
        if top_ul:
            for li in top_ul.find_all("li", recursive=False):  # Only direct children
                a = li.find("a")
                if a and a.has_attr("href") and a.text:
                    section_id = a["href"].lstrip("#")
                    section_title = a.get_text(strip=True)
                    sections.append((section_id, section_title))

        page.top_toc = sections


def attach_nav_pages(_):
    """Attach list of output paths of pages inside the specified pages_folder."""
    for page in all_pages:
        pages_folder_meta = page.metadata.get('linkedfolder')
        if not pages_folder_meta:
            continue

        # Get content root directory from settings
        content_root = Path(page.settings['PATH']).resolve()

        # pages_folder path relative to content root
        pages_folder_abs = (content_root / pages_folder_meta).resolve()

        # Safety check (ensure it's inside content root)
        try:
            pages_folder_abs.relative_to(content_root)
        except ValueError:
            continue  # skip paths outside content root

        # Find all pages whose source file is inside that pages_folder
        related_pages = []
        for other_page in all_pages:
            if other_page is page:
                continue
            other_path = Path(other_page.source_path).resolve()
            if pages_folder_abs in other_path.parents:
                related_pages.append(other_page)

        # Sort by date if available (fall back to no sort if missing)
        try:
            related_pages.sort(key=lambda p: p.date, reverse=False)  # oldest first
        except AttributeError:
            pass  # not all pages may have dates

        page.linked_pages = related_pages
        extract_top_toc(related_pages)


def register():
    signals.page_generator_finalized.connect(collect_pages)
    signals.all_generators_finalized.connect(attach_nav_pages)
