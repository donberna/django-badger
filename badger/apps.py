from django.apps import AppConfig
from actstream import registry

class BadgeConfig(AppConfig):
    name = 'badger'
    verbose_name = "Badge"

    def ready(self):
        registry.register(
        	self.get_model('Badge'))