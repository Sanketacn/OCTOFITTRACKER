from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octofit_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        octofit_models.User.objects.all().delete()
        octofit_models.Team.objects.all().delete()
        octofit_models.Activity.objects.all().delete()
        octofit_models.Leaderboard.objects.all().delete()
        octofit_models.Workout.objects.all().delete()

        # Create teams
        marvel = octofit_models.Team.objects.create(name='Marvel')
        dc = octofit_models.Team.objects.create(name='DC')

        # Create users
        users = [
            octofit_models.User(email='ironman@marvel.com', name='Iron Man', team=marvel),
            octofit_models.User(email='captain@marvel.com', name='Captain America', team=marvel),
            octofit_models.User(email='batman@dc.com', name='Batman', team=dc),
            octofit_models.User(email='superman@dc.com', name='Superman', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            octofit_models.Activity(user=users[0], type='Run', duration=30),
            octofit_models.Activity(user=users[1], type='Swim', duration=45),
            octofit_models.Activity(user=users[2], type='Bike', duration=60),
            octofit_models.Activity(user=users[3], type='Yoga', duration=20),
        ]
        for activity in activities:
            activity.save()

        # Create workouts
        workouts = [
            octofit_models.Workout(name='Morning Cardio', description='Cardio session for all heroes'),
            octofit_models.Workout(name='Strength Training', description='Strength session for all heroes'),
        ]
        for workout in workouts:
            workout.save()

        # Create leaderboard
        leaderboard = [
            octofit_models.Leaderboard(user=users[0], points=100),
            octofit_models.Leaderboard(user=users[1], points=90),
            octofit_models.Leaderboard(user=users[2], points=95),
            octofit_models.Leaderboard(user=users[3], points=85),
        ]
        for entry in leaderboard:
            entry.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
