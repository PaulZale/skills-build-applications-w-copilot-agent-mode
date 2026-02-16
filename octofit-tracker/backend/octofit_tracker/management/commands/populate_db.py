from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from djongo import models

from django.conf import settings

import random

# Sample data
USERS = [
    {"username": "ironman", "email": "ironman@marvel.com", "first_name": "Tony", "last_name": "Stark"},
    {"username": "spiderman", "email": "spiderman@marvel.com", "first_name": "Peter", "last_name": "Parker"},
    {"username": "batman", "email": "batman@dc.com", "first_name": "Bruce", "last_name": "Wayne"},
    {"username": "superman", "email": "superman@dc.com", "first_name": "Clark", "last_name": "Kent"},
]

TEAMS = [
    {"name": "Marvel", "members": ["ironman", "spiderman"]},
    {"name": "DC", "members": ["batman", "superman"]},
]

ACTIVITIES = [
    {"user": "ironman", "activity": "Running", "duration": 30},
    {"user": "spiderman", "activity": "Cycling", "duration": 45},
    {"user": "batman", "activity": "Swimming", "duration": 60},
    {"user": "superman", "activity": "Flying", "duration": 120},
]

LEADERBOARD = [
    {"user": "superman", "score": 1000},
    {"user": "batman", "score": 800},
    {"user": "ironman", "score": 700},
    {"user": "spiderman", "score": 600},
]

WORKOUTS = [
    {"name": "Full Body", "suggestion": "Pushups, Squats, Plank"},
    {"name": "Cardio", "suggestion": "Running, Cycling"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        db.users.insert_many(USERS)
        db.users.create_index([('email', 1)], unique=True)
        # Insert teams
        db.teams.insert_many(TEAMS)
        # Insert activities
        db.activities.insert_many(ACTIVITIES)
        # Insert leaderboard
        db.leaderboard.insert_many(LEADERBOARD)
        # Insert workouts
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
