# Temp_and_hum_thingspeak
A simple script to read temperature and humidity from a DHT22 and post the data to Thingspeak using rPi 3 and Python 3.

Many methods of reading a DHT sensor and/or posting data to Thingspeak using Python are overly complicated. This short script offers an uncomplicated way to read data and post it to a Thingspeak channel. It could readily be amended to offer more sophistication, but it is a great starting point for someone wanting only the basics.

You'll need the Adafruit DHT library to make this work. Find it at https://github.com/adafruit/Adafruit_Python_DHT. So far, it works as is on rPi 3 using Python 3.
