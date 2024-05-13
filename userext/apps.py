#userext/apps.py
from django.apps import AppConfig


class UserextConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userext'
    
    def ready(self):
        import userext.signals 
