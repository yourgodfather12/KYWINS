import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace 'your_project_name' with the actual name of your Django project

application = get_wsgi_application()
