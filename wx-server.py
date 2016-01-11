#!/usr/bin/env python

import os

from ambient_wx import AmbientWx

from flask import Flask, render_template
app = Flask(__name__)

WX_HOST = os.getenv("WX_HOST")
DEBUG = os.getenv("WX_DEBUG", False)

@app.route("/")
def dashboard():

    wx = AmbientWx(WX_HOST)

    return render_template("dashboard.html",
        current_time = wx.time,

        outdoor_temp = wx.outdoor_temp,
        outdoor_humidity = wx.outdoor_humidity,
        abs_pressure = wx.abs_pressure,
        solar_radiation = wx.solar_radiation,

        indoor_temp = wx.indoor_temp,
        indoor_humidity = wx.indoor_humidity,

        stale = wx.stale,
    )

if __name__ == "__main__":

    if not WX_HOST:
        raise Exception("Undefined environment variable WX_HOST")

    app.run(debug=DEBUG)

