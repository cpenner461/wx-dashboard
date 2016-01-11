#!/usr/bin/env python

import logging

from lxml import html
import requests

class AmbientWx():
    """A simple class for scraping the Ambient Weather Observer IP live data"""

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def _find(self, label):

        if not self.stale:
            elements = self.tree.xpath('//input[@name="%s"]' % label)
            return elements[0].value if elements else "n/a"
        else:
            return "--"

    def _get_data(self):
        """get data from host with simple caching"""

        try:
            r = requests.get(self.data_url)
            self.tree = html.fromstring(r.content)
            self.stale = False
        except Exception, e:
            logging.error("Uh-oh ...\n%s" % e)
            self.stale = True


    def _load(self):

        self._get_data()

        self.time = self._find("CurrTime")

        self.indoor_temp = self._find("inTemp")
        self.indoor_humidity = self._find("inHumi")

        self.abs_pressure = self._find("AbsPress")
        self.rel_pressure = self._find("RelPress")

        self.outdoor_temp = self._find("outTemp")
        self.outdoor_humidity = self._find("outHumi")

        self.wind_direction = self._find("windir")
        self.wind_speed = self._find("avgwind")
        self.wind_gust = self._find("gustspeed")

        self.solar_radiation = self._find("solarrad")
        self.uv = self._find("uv")
        self.uvi = self._find("uvi")

        self.rain_hourly = self._find("rainofhourly")

    def __init__(self, host):

        self.host = host
        self.data_url = self.host + "/livedata.html"
        self._load()

    def __str__(self):
        return("""
Host                : {host}
Time                : {time}
Indoor Temperature  : {indoor_temp}
Indoor Humidity     : {indoor_humidity}
Outdoor Temperature : {outdoor_temp}
Outdoor Humidity    : {outdoor_humidity}
Wind Direction      : {wind_direction}
Wind Speed          : {wind_speed}
Wind Gust           : {wind_gust}
""".format(**self.__dict__))

