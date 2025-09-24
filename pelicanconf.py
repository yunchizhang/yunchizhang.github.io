AUTHOR = 'Yunchi Zhang'
SITENAME = "Yzowledge"
SITEURL = ""

PATH = "content"

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/yunchi-zhang-1b26a59"),
    ("Github", "https://github.com/archer-yz"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

OUTPUT_RETENTION = [".hg", ".git", "CNAME"]
THEME = "../pelican-themes/elegant"
DIRECT_TEMPLATES = ['search', '404', 'index', 'categories', 'tags', 'archives']
# Plugins and extensions
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    'liquid_tags', 'md_include', 'neighbors', 'photos', 'related_posts',
    'render_math', 'series', 'webassets', 'extract_toc', 'linked_pages',
]
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        'markdown.extensions.toc': {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.attr_list": {},
        "markdown.extensions.def_list": {},
        "markdown.extensions.tables": {},
    },
}

TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"

ARTICLE_URL = "posts/{slug}.html"
ARTICLE_SAVE_AS = "posts/{slug}.html"
PAGES_URL = "pages/{slug}.html"
PAGES_SAVE_AS = "pages/{slug}.html"

LANDING_PAGE_TITLE = "Yunchi Zhang, PhD"

SOCIAL_PROFILE_LABEL = 'Stay in Touch'

USE_SHORTCUT_ICONS = True
STATIC_PATHS = ['theme/images', 'images',
                'digital_related/images',
                'antenna/monopulse/images',
                ]
PAGE_PATHS = ['pages', 'antenna']

# projects
PROJECTS = [
    {
        'name': 'Jitter Analyzer',
        'url': '#',
        'description': 'Jitter Analyzer can perform jitter measurement, jitter trend, jitter decomposition, ' +
        'histogram, spectrum display, eye diagram analysis, etc. on clock or symbol signals. ' +
        'Jitter Analyzer is developed in Python language.',
    },
    {
        'name': 'fecPy',
        'url': '#',
        'description': 'fecPy is a Python library for Forward Error Correction (FEC) codes. ' +
        'It provides implementations of various FEC codes, including Reed-Solomon, LDPC, and Turbo codes.',
    }
]
PROJECTS_TITLE = "Related Projects"

# comment
DISQUS_SITENAME = "yunchizhang"

# license
SITE_LICENSE = """All Rights Reserved. Copyright © 2025 <a href="mailto:yunchi.zhang@gmail.com">Yunchi Zhang</a>."""
SITESUBTITLE = "Knowledge and Experience"
