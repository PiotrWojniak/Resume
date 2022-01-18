"""Imports"""
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_courses")
def get_courses():
    """Course render function"""
    courses = list(mongo.db.courses.find().sort("added", 1))
    courses.reverse()
    return render_template("courses.html", courses=courses)


# View course information function
@app.route("/view_course/<course_id>")
def view_course(course_id):
    course = mongo.db.courses.find_one({"_id": ObjectId(course_id)})
    return render_template("view_course.html", course=course)


@app.route("/get_works")
def get_works():
    """Course render function"""
    works = list(mongo.db.courses.find().sort("added", 1))
    works.reverse()
    return render_template("works.html", works=works)


# View course information function
@app.route("/view_work/<work_id>")
def view_work(work_id):
    work = mongo.db.works.find_one({"_id": ObjectId(work_id)})
    return render_template("view_work.html", work=work)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
