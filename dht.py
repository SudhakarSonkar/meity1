import Adafruit_DHT
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

current_time = now.strftime("%H:%M:%S")

now = datetime.now()
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://meity-40d5f-default-rtdb.firebaseio.com/'
    })

ref = db.reference('/')
ref.set({
    current_time, "Temperature: ", temperature,
    current_time, "Humidity: ", humidity,
    })






print("Current Time =", current_time)

'''
ref = db.reference('Temerature')
ref.update({
    'Temerature':temerature,
    'Humidity':humidity,
})
'''