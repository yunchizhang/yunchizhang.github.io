linked_pages
==================

This a Pelican plugin.

* Allows a page to navigate the linked pages in a folder.
* It is developed primarily for a page template to link to multiple pages.

## How to Use

1. Group linked pages, Markdown or reStructuredText format, into a folder. Set `status`
   to `hidden` for each page.
2. Create a simple page template (e.g. simple_page.html) to generate the linked pages.
3. Create a page that is meant to contain all the linked pages.
4. Add a metadata item `linkedfolder` to indicate the relative folder path having the linked pages. For example,

		linkedfolder: pages/linked_pages

5. Create a page template (e.g. nav_page.html) and inform Pelican to use the template for the page.

		template: nav_page

6. The page template has access to a list of the linked page objects. The linked pages are sorted
   based on the created date.

		page.linked_pages

7. If a table of content is extracted in each linked page using Pelican plugin `extract_toc`, a
   list of tuples will be created to save the sections in the page as [(section_id, section_title),
   ...]. It can be used for sub-links for each page.

		page.top_toc

## Examples

### Template: nav_page.html

	{% for p in page.linked_pages %}
	<div class="nav-link" data-file="{{ SITEURL }}/{{ p.url }}">{{ p.title }}</div>
		{% if p.top_toc %}
		<div class="submenu">
			{% for section_id, section_title in p.top_toc %}
			<a href="#{{ section_id }}">{{ section_title }}</a>
			{% endfor %}
		</div>
		{% endif %}
	{% endfor %}

### pages/top_page.md

	title: Top Page
	linkedfolder: pages/linked_pages
	template: nav_page

### pages/linked_pages/page1.md

	title: Page 1
	template: simple_page
	status: hidden

### pages/linked_pages/page2.md

	title: Page 2
	template: simple_page
	status: hidden

## Recommendation

It is recommended to use this extension along with the `extrac_toc` plugin so that sub-links in
each linked page can be created in the top page.
