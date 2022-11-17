# app.py file for Flask App

from flask import Flask

#Create the app
app = Flask(__name__)

#Create a homepage for the app
@app.route("/")
#When we go to our URL.com/
  # Then flask will run this function below

  # In our function, we will "return" 
  # the HTML that we want flask to serve
def helloWorld():
  return "<h1>My Name is Aaron Ratliff</h1>"