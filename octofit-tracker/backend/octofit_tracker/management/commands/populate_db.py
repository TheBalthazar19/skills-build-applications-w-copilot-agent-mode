from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel.name)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc.name)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc.name)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, date=date.today())
        Activity.objects.create(user=batman, type='cycle', duration=45, date=date.today())
        Activity.objects.create(user=superman, type='swim', duration=60, date=date.today())
        Activity.objects.create(user=captain, type='walk', duration=20, date=date.today())

        # Create workouts
        w1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        w2 = Workout.objects.create(name='Situps', description='Do 30 situps', difficulty='medium')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100, rank=1)
        Leaderboard.objects.create(user=batman, score=90, rank=2)
        Leaderboard.objects.create(user=superman, score=80, rank=3)
        Leaderboard.objects.create(user=captain, score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
