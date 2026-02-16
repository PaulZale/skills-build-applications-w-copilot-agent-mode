from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
        self.assertEqual(user.username, 'testuser')

    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam', members=['testuser'])
        self.assertEqual(team.name, 'TestTeam')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='testuser', score=100)
        self.assertEqual(lb.score, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', suggestion='Pushups')
        self.assertEqual(workout.name, 'TestWorkout')
