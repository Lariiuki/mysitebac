# Contém propriedades de configuração WSGI para o projeto Django. Basicamente, o script Python usado para ajudar a executar seu servicor de desenvolvimento e implantar seu proejto em um ambiente de produção

"""
WSGI config for mysitebac project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysitebac.settings')

application = get_wsgi_application()
