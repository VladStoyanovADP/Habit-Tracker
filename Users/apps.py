from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'

class RewardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Rewards'
    
class HabitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Habits'