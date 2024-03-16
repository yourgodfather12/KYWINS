from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app_name'  # Replace 'your_app_name' with the actual name of your Django app
    verbose_name = 'Your App Name'  # Add a custom verbose name for your app
