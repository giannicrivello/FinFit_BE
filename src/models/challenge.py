import mongoengine

class Challenge(mongoengine.Document):
    #list challenge model
    intensity_score = mongoengine.IntField()
    workout_type = mongoengine.StringField()
    workout_name = mongoengine.StringField()
    
    meta = {
        'db_alias': 'core',
        'colleciton': 'challenge'
    }