import dht
from machine import Pin

sensor = dht.DHT11(Pin(22))  # Change the pin number based on your wiring
# sensor.measure()

temperature = sensor.temperature()
humidity = sensor.humidity()

print(temperature)
