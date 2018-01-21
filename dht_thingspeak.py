import Adafruit_DHT as dht # DHT library to allow reading from the sensor.
from datetime import datetime # For timestamps.
from time import sleep # For delays between loops.
import urllib.request # For basic connection to the Thingspeak API to post to a channel.

loop = True
counter = 0
dest = 'https://api.thingspeak.com/update?api_key=' # Main URL, custom strings to follow.
key = 'YOUR_WRITE_KEY_HERE' # Thingspeak channel write key.

while loop:
    h,t = dht.read_retry(dht.DHT22,4) # Read temp and humidity from GPIO pin 4.
    f1 = '&field1={:.1f}'.format(t) # Place temperature data in field 1, to be added to URL.
    f2 = '&field2={:.1f}'.format(h) # Place humidity data in field 2, to be added to URL.
    data_file = open('temp_hum_log.txt', 'a') # Open local file in append mode.
    ts = datetime.now() # Get timestamp for current loop.
    data_file.write('Temp={:.1f}*C Humidity={:.1f}% Time={}\n'.format(t,h,ts)) # Write log to local file whether online post succeeds or not.
    try: # In case something is wrong with the connection, we'll keep running.
        post = urllib.request.urlopen(dest + key + f1 + f2) # Concatenate URL, store as variable post.
        print('Temp={:.1f}*C Humidity={:.1f}%'.format(t,h)) # Print result to Shell.
        response = post.read() # Get response ('0' = failure.)
        print(response) # For real-time debugging.
    except:
        print('Connection failed.')
        data_file.write('Connection failed at {}.\n'.format(ts)) # Log failed connections.
    data_file.close()
    counter += 1
    sleep(59) # Loop seems to take about 1 second, giving us a nicer total delay time.
#    if counter >= 100: # If a post limit is desired.
#        loop = False
