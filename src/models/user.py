import json
import mongoengine

class User(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    username = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True) #dont forget to encrypt this
    height = mongoengine.FloatField(required=True)
    weight = mongoengine.FloatField(required=True)

    #we should pre compute these attributes during a users session
    #I plan to have them stored as a list of tuples (date_time, cycles)
    #cycles will be a sensor on the user and we wont have this data until user starts the workout
    start_session = mongoengine.ListField() 
    end_session = mongoengine.ListField()
     
    #this will also be computed as soon as the user is done with their session 
    #We should make a call to the last two start and end sessions and unpack the data to access 
    #rate, count, etc
    recorded_score = mongoengine.ListField() #this should also be stored as a list of tuples (date, score).

    #a list of all the challenges a user has completed
    challenges_completed = mongoengine.EmbeddedDocumentListField()


    meta = {
        'db_alias': 'core',
        'collection': 'user'
    }

