from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class StringIdModelSerializer(serializers.ModelSerializer):
    # Djongo/MongoDB pode expor IDs como ObjectId; sempre serializamos como string.
    id = serializers.CharField(source='pk', read_only=True)


class TeamSerializer(StringIdModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserProfileSerializer(StringIdModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class ActivitySerializer(StringIdModelSerializer):
    user_name = serializers.CharField(source='user.hero_name', read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'


class LeaderboardEntrySerializer(StringIdModelSerializer):
    user_name = serializers.CharField(source='user.hero_name', read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = '__all__'


class WorkoutSuggestionSerializer(StringIdModelSerializer):
    user_name = serializers.CharField(source='user.hero_name', read_only=True)

    class Meta:
        model = WorkoutSuggestion
        fields = '__all__'
