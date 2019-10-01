import os
from app import app
from flask import render_template, request, redirect

# username = "period8"
#
# # events = [
# #         {"event":"First Day of Classes", "date":"2019-08-21"},
# #         {"event":"Winter Break", "date":"2019-12-20"},
# #         {"event":"Finals Begin", "date":"2019-12-01"},
# #         {"event": "Summer Vacation", "date": "2020-06-03"}
    #]


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

#this connects to the ebare+ex@dwight.edu account
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:Bxa3Y6a9Wha2tDay@cluster0-dy5sy.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX


@app.route('/index')

def index():
    #connect to database
    collection = mongo.db.events
    #query the database to get all of the events
    event = list(collection.find({}))
    #print(event)

    return render_template('index.html', events = event)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    test = mongo.db.test
    # insert new data
    test.insert({'name': 'last day of school'})
    # return a message to the user
    return "Added data to database!"

@app.route('/input')
def input():
    return render_template('input.html')

# Create a route for ‘/results’ that stores the data from the form
@app.route('/results', methods = ["Get", "Post"])
def results():
    #Get userdata from the form
    userdata = dict(request.form)
    print(userdata)
    # Store the event_name and event_date as separate variables
    event_name = userdata['event_name']
    #print(event_name)
    event_date = userdata['event_date']
    #event type
    event_type = userdata['event_type']
    #print(event_date)
    # Connect to your Mongo cluster and collection and a database called events.
    events = mongo.db.events
    # Insert the name and date of the event to your Mongo events database as a dictionary {“name”: event_name, “date”: event_date}
    events.insert({"name": event_name, "date": event_date,"type": event_type})
    return redirect("/index")

# @app.route('/input')
# def input():
#     #check our HTML file to see if form appears
#     return render_template('input.html')

# @app.route('/results', methods = ["GET", "POST"])
# def results():
#     userdata = dict(request.form)
#     print(userdata)
#     event_name = userdata["name"]
#     print(event_name)
#     event_date = userdata["date"]
#     print(event_date)
#     #connect to Mongo DB
#     collection = mongo.db.events
#     #insert data to events database
#     collection.insert({"name": event_name, "date": event_date})
#     #return a value to the user
#     return "you added data to database"
