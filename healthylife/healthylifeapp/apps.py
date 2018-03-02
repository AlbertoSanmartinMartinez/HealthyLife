from django.apps import AppConfig

class PostAppConfig(AppConfig):
    name = 'healthylife'

    def ready(self):
        pre_save.connect(createSlug, dender=self)
