from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_caching import Cache


app=Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config.from_object('config.BaseConfig')  # Set the configuration variables to the flask application
cache = Cache(app)
api=Api(app)

def host():
     app.run(port=7002,debug=True,host = "0.0.0.0")


