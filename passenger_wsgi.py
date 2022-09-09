import os
import sys

sys.path.insert(0, '/home/h53456c/public_html/zdravo_app')
sys.path.insert(1, '/home/h53456c/virtualenv/public_html/zdravo_app/3.9/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ZDRAVO_clinic_web.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
