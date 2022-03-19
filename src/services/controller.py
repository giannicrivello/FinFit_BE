from tokenize import String
from typing import List, Optional


from models.challenge import Challenge
from models.leaderboard import LeaderBoard
from models.user import User


#create a new use
def create_account(name: str, username: str, password: str, height: float, weight: float) -> User:
    user = User()
    user.name = name
    user.username = username
    user.password = password
    user.height = height
    user.weight = weight
    user.start_session = []
    user.end_session = []
    user.recorded_score = []
    user.challenges_completed = []

    user.save()
    return user

def create_challenge(intensity_score: int, workout_type: str, workout_name: str) -> Challenge:
    challenge = Challenge()
    challenge.intensity_score = intensity_score
    challenge.workout_type = workout_type
    challenge.workout_name = workout_name
    
    challenge.save()
    return challenge