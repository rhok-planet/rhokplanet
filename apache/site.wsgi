import os, sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace) 

os.environ['DJANGO_SETTINGS_MODULE'] = 'rhokplanet.settings'
from django.conf import settings
sys.path.insert(0, os.path.join(settings.PROJECT_ROOT, "apps"))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
