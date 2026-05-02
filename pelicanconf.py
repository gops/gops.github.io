AUTHOR = 'Gopal Patel'
SITENAME = "Gopal's Website"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Calcutta'

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
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/iamgopal/"),
    ("GitHub", "https://github.com/iamgopal"),
    ("Twitter", "https://twitter.com/iamgopal"),
)

DEFAULT_PAGINATION = 10

# Static files configuration
STATIC_PATHS = ['extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Template configuration
THEME_TEMPLATES_OVERRIDES = ['content/theme/templates']

# Use relative URLs for development
RELATIVE_URLS = True
