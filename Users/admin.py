from django.contrib import admin
from .models import Rewards, Habits


@admin.register(Rewards)
class RewardsAdmin(admin.ModelAdmin):
    list_display = ('rewards_name', 'rewards_description', 'rewards_cost', 'user_id')

@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ('habit_name', 'habit_category', 'habit_type', 'habit_streak', 'user_id')
    
    