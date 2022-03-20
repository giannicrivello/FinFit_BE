from os import name
from flask import Flask, request
from flask_restful import Resource, Api
from services.controller import create_account, create_challenge
from services.auth import find_account_by_username, find_account_by_password
import models.mongo_setup as mongo_setup 
from models.user import User
import datetime


app = Flask(__name__)
api = Api(app)

#[DEFINE MONGODB CONNECTION]
def main():
    mongo_setup.global_init()

#[ERROR MESSAGE]
def err(string: str) -> str:
    return string

#[API CALLS]
user_endpoints = [] #mutable set
challenge_endpoints = [] 

#[ADD USER]
@app.route('/sign_up/<string:user_id>', methods = ['POST'])
def add_user(user_id):
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
    user_endpoints.append(user_id)
    user = create_account(name, username, password, height, weight)
    return f"Added User {user.name}"

#[START SESSION]
@app.route("/log/start_session/<string:username>", methods=['GET', 'POST'])
#how do i pass a param from the request to the application
def log_start_session(username) -> str:
    for i in User.objects(username=username):
        #set the value of User.start_session: list[]
        i.start_session.append(datetime.datetime.now)
        return f'{i.name} started session'

#[END SESSION]
@app.route("/log/end_session/<string:username>", methods=['GET', 'POST'])
#how do i pass a param from the request to the application
def log_start_session(username) -> str:
    for i in User.objects(username=username):
        #set the value of User.end_session: list[]
        i.end_session.append(datetime.datetime.now)
        return f'{i.name} ended session'

#[DAILY_CHALLENGE]
@app.route("/challenges/daily", methods=['GET'])
def get_daily_challenges():
    pass

#[LOG CHALLENGE]
@app.route("/log/challenges", methods=['GET', 'POST'])
def log_daily_challenges():
    pass


#[GET ALL USERS]
@app.route("/users", methods=['GET'])
def get_users() -> dict[User]:
    users = {}
    for i in User.objects().all():
        users['name'] = i.name
        users['username'] = i.username
        users['password'] = i.password
        users['height'] = i.height
        users['weight'] = i.weight
        users['start_session'] = i.start_session
        users['end_session'] = i.end_session
        users['recorded_score'] = i.recorded_score
        users['challenges_completed'] = i.challenges_completed
        return users 

#[LEADER BOARD]
@app.route("/leaderboard", methods=['GET'])
def list_of_top_users() -> list[User]:
    users = {}

    for i in User.objects(): #query for top users
        users['name'] = i.name
        users['username'] = i.username
        users['password'] = i.password
        users['height'] = i.height
        users['weight'] = i.weight
        users['start_session'] = i.start_session
        users['end_session'] = i.end_session
        users['recorded_score'] = i.recorded_score
        users['challenges_completed'] = i.challenges_completed
        return users 


#[ADD CHALLENGE]
@app.route("/admin/add_challenge/<string:challenge_id>", methods = ['POST'])
def add_challenge(challenge_id):
    intensity_score = request.form['intensity_score']
    workout_type = request.form['workout_type']
    workout_name =request.form['workout_name']
    challenge = create_challenge(intensity_score, workout_type, workout_name)
    challenge_endpoints.append(challenge_id)
    return f"Added Challenge {challenge.workout_name}"

#[RESOURCE ADD]
#api.add_resource(AddUser, '/sign_up/<string:user_id>')
#api.add_resource(Admin, '/admin/<string:challenge_id>')

if __name__ == '__main__':
    main()
    app.run(debug=True)
