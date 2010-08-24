import os, sys
import calloway
from calloway.settings import *

CALLOWAY_ROOT = os.path.abspath(os.path.dirname(calloway.__file__))
sys.path.insert(0, os.path.join(CALLOWAY_ROOT, 'apps'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SVN_DIR = os.path.dirname(__file__)
ADMINS = (
     ('Justin Quick', 'justquick@gmail.com'),
)

MANAGERS = ADMINS + ( ('Barbara Beelar', 'bbeelar@rcn.com'), )
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(SVN_DIR,'data.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/justquick/friendsofdcl.org/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://friendsofdcl.org/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/static/admin/'


try:
    from local_settings import MEDIA_URL_PREFIX
except ImportError:
    MEDIA_URL_PREFIX = "/media/"
try:
    from local_settings import MEDIA_ROOT_PREFIX
except ImportError:
    MEDIA_ROOT_PREFIX = './media'
try:
    from local_settings import MEDIA_ROOT
except ImportError:
    MEDIA_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'ugc')
try:
    from local_settings import STATIC_ROOT
except ImportError:
    STATIC_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'static')
    

MEDIA_URL = '%sugc/' % MEDIA_URL_PREFIX
STATIC_URL = "%sstatic/" % MEDIA_URL_PREFIX
STATIC_MEDIA_APP_MEDIA_PATH = STATIC_ROOT
STATIC_MEDIA_COPY_PATHS = (
    {'from': os.path.join(CALLOWAY_ROOT, 'media'), 'to': STATIC_ROOT},
    {'from': 'static', 'to': STATIC_ROOT},
)
STATIC_MEDIA_COMPRESS_CSS = not DEBUG
STATIC_MEDIA_COMPRESS_JS = not DEBUG
STATIC_MEDIA_PURGE_OLD_FILES = False


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ma4y*&7i_a=#&s1asdfaasfdsdfj$om2503&7=#8-wtv(ah+ur4ofy_pk8qg5h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'ban.middleware.DenyMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(SVN_DIR,'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

INSTALLED_APPS = APPS_CORE + \
	    APPS_ADMIN + \
	    APPS_STAFF + \
	    APPS_REVERSION + \
	    APPS_STORIES + \
	    APPS_CALLOWAY_DEFAULT + \
	    APPS_MPTT + \
	    APPS_CATEGORIES + \
	    APPS_COMMENT_UTILS + \
	    APPS_FRONTEND_ADMIN + \
	    APPS_MEDIA + \
	    APPS_UTILS + \
	    APPS_REGISTRATION + \
	    APPS_TINYMCE + (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'mail',
    'registration',
)
INSTALLED_APPS = list(INSTALLED_APPS)

INSTALLED_APPS[INSTALLED_APPS.index('synagg')]

ACCOUNT_ACTIVATION_DAYS = 7


#AUTH_PROFILE_MODULE = 'mail.Profile'
try: from local_settings import *
except ImportError: pass
