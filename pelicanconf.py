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
# PLUGINS = [
#     'series',
#     'tipue_search',
#     'render-math',
# ]
DIRECT_TEMPLATES = ['search', '404', 'index', 'categories', 'tags', 'archives']
# Plugins and extensions
# MARKDOWN = {
#     "extension_configs": {
#         "markdown.extensions.extra": {},
#         "markdown.extensions.meta": {},
#         'markdown.extensions.toc': {}
#     }
# }


TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"

LANDING_PAGE_TITLE = "Yunchi Zhang, PhD"

SOCIAL_PROFILE_LABEL = 'Stay in Touch'

USE_SHORTCUT_ICONS = True
STATIC_PATHS = ['theme/images', 'images']

# projects
PROJECTS = [
    {
        'name': 'Jitter Analyzer',
        'url': '#',
        'description': 'Jitter Analyzer can perform jitter measurement, jitter trend, jitter decomposition, ' + \
            'histogram, spectrum display, eye diagram analysis, etc. on clock or symbol signals. ' + \
            'Jitter Analyzer is developed in Python language.',
    },
    {
        'name': 'fecPy',
        'url': '#',
        'description': 'fecPy is a Python library for Forward Error Correction (FEC) codes. ' + \
            'It provides implementations of various FEC codes, including Reed-Solomon, LDPC, and Turbo codes.',
    }
]
PROJECTS_TITLE = "Related Projects"

# comment
DISQUS_SITENAME = "yunchizhang"
