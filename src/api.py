from flask import Flask, request
from flask_restful import Resource, Api
from services.controller import create_account, create_challenge
from services.auth import find_account_by_username, find_account_by_password
import models.mongo_setup as mongo_setup 
from models.user import User
from typing import List

app = Flask(__name__)
api = Api(app)

#[DEFINE MONGODB CONNECTION]
def main():
    mongo_setup.global_init()

#[ERROR MESSAGE]
def err(string: str) -> str:
    return string



#[API CALLS]
user_endpoints = {} #mutable set
challenge_endpoints = {} 

class AddUser(Resource):
    def put(self, user_id):
        name = request.form['name']
        username = request.form['username']
        #still need to encrypt
        password = request.form['password']
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        #query for existing username
        existing_username = find_account_by_username(username)
        print(existing_username)
        #query for existing password
        existing_password = find_account_by_password(password)
        if existing_username:
            error = err(f"Account with username or password already exists.")
            return {'ERROR': f'{error}'}
        if existing_password:
            error = err(f"Accout with username of password already exists")
            return {'ERROR': f'{error}'}
        
        #storing user_id from endpoint request
        user_endpoints.push(user_id)
        
        user = create_account(name, username, password, height, weight)
        return f"Added User {user.name}"

class StartSession(Resource):
    pass

class EndSession(Resource):
    pass

class RecordScore(Resource):
    pass

class LogChallenge(Resource):
    pass

class LeaderBoard(Resource):
    def get(self):
        list_of_top_users()

def list_of_top_users(user_score: int) -> List[User]:
    users = []
    #this needs to be fixed
    for i in User.objects(recorded_score = user_score).get_all().sort()[0:100]:
        users.append(i)
    return users


#used for adding challanges
class Admin(Resource):
    def put(self, challenge_id):
        intensity_score = request.form['intesity_score']
        workout_type = request.form['workout_type']
        workout_name =request.form['workout_name']
        challenge = create_challenge(intensity_score, workout_type, workout_name)

        challenge_endpoints.push(challenge_id)
        return f"Added Challenge {challenge.name}"

#[RESOURCE ADD]
api.add_resource(AddUser, '/sign_up/<string:user_id>')
api.add_resource(Admin, '/admin/<string:challenge_id>')

if __name__ == '__main__':
    main()
    app.run(debug=True)
