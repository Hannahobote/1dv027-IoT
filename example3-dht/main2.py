from machine import Pin
import utime as time
from dht import DHT11

# The GPIO number is 13 which is equal to the pin number 17
pin = Pin(13, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    time.sleep(2)
    try:
        sensor.measure()  # Measure the sensor values
        t = sensor.temperature()
        h = sensor.humidity()
        print("Temperature: {:.1f} °C".format(t))
        print("Humidity: {:.1f} %".format(h))
    except:
        print("An exception occurred")
        continue
