"""Imports"""
import os
from flask import Flask
if os.path.exists("env.py"):
    import env

"""Flask instance"""
app = Flask(__name__)

"""Test function"""
@app.route("/")
def test():
    return "Hello world"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
