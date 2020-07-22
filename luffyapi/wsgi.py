"""
WSGI config for luffyapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
# 修改setting文件的位置--settings文件夹-dev，上线后改为pro

application = get_wsgi_application()
