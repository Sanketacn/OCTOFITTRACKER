from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        Activity.objects.create(user=ironman, type='Run', duration=30)
        Workout.objects.create(name='Morning Cardio', description='Cardio session')
        Leaderboard.objects.create(user=ironman, points=100)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 2)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
