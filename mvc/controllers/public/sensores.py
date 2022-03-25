import web
import app
import pyrebase
import firebase_config as token
import json

class Sensores:
    def GET(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        db = firebase.database()
        sensores = db.child("sensores").get()
        result = json.dumps(sensores.val())
        return result