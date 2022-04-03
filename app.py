"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import get_nearest_station


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/result', methods=["GET", "POST"])
def nearestStation():
    if request.method == "POST":
        return "hello world"
        placeName = request.form["placeName"]
        nearest_station, isAccessible = get_nearest_station(placeName)
        return render_template("result.html", placeName = placeName, nearestStation = nearestStation, isAccessible = isAccessible)
    else:
        return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)