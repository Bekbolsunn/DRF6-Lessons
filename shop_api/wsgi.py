"""
WSGI config for shop_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_api.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    print(f"ОШИБКАААААААААААААААААААААААА: {e}")
    raise e