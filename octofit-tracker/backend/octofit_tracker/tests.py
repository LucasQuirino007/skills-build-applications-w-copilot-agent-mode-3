from django.test import TestCase

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class OctoFitApiTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Guardians', universe='Marvel')
        self.user = UserProfile.objects.create(
            name='Peter Parker',
            email='peter@example.com',
            hero_name='Spider-Man',
            team=self.team,
        )
        Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration_minutes=45,
            calories_burned=350,
        )
        LeaderboardEntry.objects.create(user=self.user, points=1500, rank=1)
        WorkoutSuggestion.objects.create(
            user=self.user,
            title='High Intensity Cardio',
            description='20 minute HIIT session focused on endurance.',
            difficulty='Medium',
        )

    def test_root_redirects_to_api(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/api/')

    def test_api_root_is_available(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIn('users', body)
        self.assertIn('teams', body)
        self.assertIn('activities', body)
        self.assertIn('leaderboard', body)
        self.assertIn('workouts', body)

    def test_collection_endpoints_return_data(self):
        endpoints = [
            '/api/users/',
            '/api/teams/',
            '/api/activities/',
            '/api/leaderboard/',
            '/api/workouts/',
        ]
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(isinstance(response.json(), list))
