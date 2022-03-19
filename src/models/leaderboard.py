import mongoengine

class LeaderBoard(mongoengine.Document):
    #list of top users user.sort()[0..n]
    top_users = mongoengine.ListField()