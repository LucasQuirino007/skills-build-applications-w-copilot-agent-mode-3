from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=120, unique=True)
    universe = models.CharField(max_length=60)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    hero_name = models.CharField(max_length=120)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'{self.hero_name} ({self.email})'


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=80)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.hero_name} - {self.activity_type}'


class LeaderboardEntry(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entry')
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank', '-points']

    def __str__(self):
        return f'#{self.rank} {self.user.hero_name} ({self.points} pts)'


class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=150)
    description = models.TextField()
    difficulty = models.CharField(max_length=40)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f'{self.title} - {self.user.hero_name}'
