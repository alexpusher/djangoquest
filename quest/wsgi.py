"""
WSGI config for quest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys 

os.environ['DJANGO_SETTINGS_MODULE'] = 'quest.settings'
sys.path.append('/data/django')
sys.path.append('/data/django/quest')

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
