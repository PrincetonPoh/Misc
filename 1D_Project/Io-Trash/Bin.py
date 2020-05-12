import RPi.GPIO as GPIO
from gpiozero import LED, Button, InputDevice, DistanceSensor
from libdw import pyrebase
from credential import *
import time

print('Initiating...')
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password(email, password)

class Bin:
    def __init__(self, ID, db, user, echoPin=24, triggerPin=23, waterPin=18, smellPin=17, buttonPin=20, LEDPin=26):
        self.ID = str(ID)
        self.US = DistanceSensor(echo=echoPin, trigger=triggerPin)
        self.water = InputDevice(waterPin)
        self.smell = InputDevice(smellPin)
        self.button = Button(buttonPin)
        self.button.when_pressed = self.button_pressed
        self.LED = LED(LEDPin)
        self.sensors = {'us': False,
                      'water': False,
                      'smell': False}
        self.needClean = self.sensors['us'] or self.sensors['water'] or self.sensors['smell'] 
        self.cleaning = False
        self.db = db
        self.user = user

    def get_data(self):
        # get ultrasonic, water and smell sensor data
        USReading = self.US.distance * 100
        print(USReading)
        waterReading = not self.water.is_active
        smellReading = self.smell.is_active
        if USReading <= 20:
            self.sensors['us'] = True
        else:
            self.sensors['us'] = False
        self.sensors['water'] = waterReading
        self.sensors['smell'] = smellReading

        currentState = self.sensors['us'] or self.sensors['water'] or self.sensors['smell']
        if currentState and not self.needClean:
            self.log(1)
        elif not currentState and self.needClean:
            self.log(0)

        self.needClean = currentState
        print(self.sensors)


    def update(self):
        # update date to firebase
        self.db.child('current_bin_states').child(self.ID).set(self.sensors, self.user['idToken'])

    def button_pressed(self):
        # check if the button is pressed, change the cleaning state accordingly
        self.cleaning = not self.cleaning
        self.LED.toggle()
        print('button pressed')

    def log(self, logType):
        # log record to firebase for analysis
        t = time.localtime(time.time())
        log = '{} {} {} {}'.format(t.tm_wday, t.tm_hour, t.tm_min, logType)
        self.db.child('log').child(self.ID).push(log, self.user['idToken'])

bin = Bin(1, db, user)

def loop():
    while True:
        if not bin.cleaning:
            t = time.localtime(time.time())
            if t.tm_sec % 3 == 1:
                bin.get_data()
               # bin.update()
                time.sleep(1)

loop()
