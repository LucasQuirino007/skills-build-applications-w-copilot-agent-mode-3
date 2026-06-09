from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class Command(BaseCommand):
    help = 'Popular o banco de dados octofit_db com dados de teste'

    def handle(self, *args, **options):
        WorkoutSuggestion.objects.all().delete()
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        marvel = Team.objects.create(name='Equipe Marvel', universe='Marvel')
        dc = Team.objects.create(name='Equipe DC', universe='DC')

        heroes = [
            {'name': 'Tony Stark', 'email': 'tony@marvel.com', 'hero_name': 'Homem de Ferro', 'team': marvel},
            {'name': 'Steve Rogers', 'email': 'steve@marvel.com', 'hero_name': 'Capitão América', 'team': marvel},
            {'name': 'Bruce Wayne', 'email': 'bruce@dc.com', 'hero_name': 'Batman', 'team': dc},
            {'name': 'Clark Kent', 'email': 'clark@dc.com', 'hero_name': 'Superman', 'team': dc},
        ]

        users = [UserProfile.objects.create(**hero) for hero in heroes]

        activities_data = [
            {'user': users[0], 'activity_type': 'Corrida', 'duration_minutes': 40, 'calories_burned': 480},
            {'user': users[1], 'activity_type': 'Ciclismo', 'duration_minutes': 50, 'calories_burned': 530},
            {'user': users[2], 'activity_type': 'Treino Funcional', 'duration_minutes': 45, 'calories_burned': 500},
            {'user': users[3], 'activity_type': 'Natação', 'duration_minutes': 35, 'calories_burned': 420},
        ]
        for activity in activities_data:
            Activity.objects.create(**activity)

        points_map = [980, 930, 910, 890]
        sorted_users = sorted(zip(users, points_map), key=lambda x: x[1], reverse=True)
        for rank, (user, points) in enumerate(sorted_users, start=1):
            LeaderboardEntry.objects.create(user=user, points=points, rank=rank)

        workout_data = [
            {
                'user': users[0],
                'title': 'Armadura Cardio',
                'description': 'Treino intervalado de alta intensidade para resistência.',
                'difficulty': 'Alta',
            },
            {
                'user': users[1],
                'title': 'Escudo Core',
                'description': 'Foco em estabilidade de core e resistência muscular.',
                'difficulty': 'Média',
            },
            {
                'user': users[2],
                'title': 'Caverna Fitness',
                'description': 'Treino funcional com circuitos de força e agilidade.',
                'difficulty': 'Alta',
            },
            {
                'user': users[3],
                'title': 'Voo Metabólico',
                'description': 'Sessão cardio para ganho de condicionamento em alta rotação.',
                'difficulty': 'Média',
            },
        ]
        for workout in workout_data:
            WorkoutSuggestion.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com sucesso.'))
