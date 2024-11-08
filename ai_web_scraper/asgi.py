"""
ASGI config for ai_web_scraper project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_web_scraper.settings')

application = get_asgi_application() 