# FinFit_BE
API written in flask and using mongodb

Api reqs:

- Add user

- Get challenges

- Start session

- End session

- Record score

- Get leaderboard

Basic arch:
- HTTP webserver to host API

- Flask api defining endpoints

- PUSH request for login (add user)

- PUSH request for recording score

- PUSH request for start session

- PUSH request for end session

- GET request for leaderboard

Models:
User
- id
- name
- height
- weight
- start_session(time series tuple (date_time, cycles))
- end_session(time series tuple(date_time, cycles))
- recorded score (for i=start_session[0]; i < end_session[0]; i++: sum = start_session[1] + end_session[1])
-chalanges_completed(List[Challenges])

Challenge
- id
- intensity
- type
- name

LeaderBoard
- Top Users (List[User.score.sort()[0..100]])
