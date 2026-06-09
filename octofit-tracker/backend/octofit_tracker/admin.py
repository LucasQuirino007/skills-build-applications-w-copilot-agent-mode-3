from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'universe')
    search_fields = ('name', 'universe')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hero_name', 'team')
    search_fields = ('name', 'email', 'hero_name')
    list_filter = ('team',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'created_at')
    search_fields = ('activity_type', 'user__hero_name', 'user__email')
    list_filter = ('activity_type', 'created_at')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'points', 'rank')
    search_fields = ('user__hero_name', 'user__email')
    list_filter = ('rank',)
    ordering = ('rank', '-points')


@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'difficulty')
    search_fields = ('title', 'difficulty', 'user__hero_name', 'user__email')
    list_filter = ('difficulty',)
