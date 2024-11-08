"""
WSGI config for ai_web_scraper project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_web_scraper.settings')

application = get_wsgi_application() 