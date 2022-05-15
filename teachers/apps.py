from django.apps import AppConfig


class TeachersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teachers'


    def ready(self):
        from .hendlers import teacher_edit_handler