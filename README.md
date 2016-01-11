# Overview
This is currently a *simple* Python dashboard that displays current weather stats
as reported by an Ambient Weather [Observer IP][OBSERVERIP] module. It will
hopefully grow into a more robust dashboard for various weather/temperature
data.

# Getting Started
This has not been optimized/tested much for this, but if you are comfortable
with Python you can do the following (preferably in a virtualenv):

    pip install -r requirements.txt

Once the requirements have been successfully installed you can run the simple
Flask server like:

    WX_HOST=http://HOSTNAME_OR_IP wx-server.py

where `WX_HOST` is the address of your Observer IP module, and then browse to
[http://localhost:5000](http://localhost:5000) to see your weather.

[OBSERVERIP]: http://www.ambientweather.com/amobserverip.html
