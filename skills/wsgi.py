import os
from django.core.wsgi import get_wsgi_application
import sys, dj_database_url
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skills.settings')
if os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

if not ((len(sys.argv) > 1) and (sys.argv[1] == 'collectstatic')):
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

application = get_wsgi_application()
