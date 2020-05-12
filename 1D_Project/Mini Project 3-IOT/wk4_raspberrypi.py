import RPi.GPIO as GPIO
from time import sleep
from libdw import pyrebase

projectid = "dw1dproject"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyCMv0kFFwAnStTfLbI94PVdppuPZAhmS_Q"  # unique token used for authentication
email = "angsonggee@yahoo.com.sg"
password = "password"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password(email, password)

# Use the BCM GPIO numbers as the numbering scheme.
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.
buttons = [12, 16, 20, 21]

# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
GPIO.setup(buttons, GPIO.IN, GPIO.PUD_DOWN)

# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []


done = False
buttons_dict = {"w": buttons[0], "a": buttons[1], "d": buttons[2], "Ok": buttons[3]}

while not done:

    # Write your code here

    '''
    We loop through the key (button name), value (gpio number) pair of the buttons
    dictionary and check whether the button at the corresponding GPIO is being
    pressed. When the OK button is pressed, we will exit the while loop and 
    write the list of movements (movement_list) to the database. Any other button
    press would be stored in the movement_list.

    Since there may be debouncing issue due to the mechanical nature of the buttons,
    we can address it by putting a short delay between each iteration after a key
    press has been detected.
    '''
    for key, value in buttons_dict.items():
        # Loop through each button in Dict
        output = GPIO.input(value)
        if output is GPIO.HIGH:
            if key != "Ok":
                movement_list.append(key)
            else:
                db.child("movement_list").set(movement_list, user['idToken'])
#                current_list = db.child("movement_list").get(user['idToken'])
#                if current_list.val() != None:
#                    new_list = current_list.val()
#                    new_list.append(movement_list)
#                    db.child("movement_list").set(new_list, user['idToken'])
#                else:
                    # Nothing in current list, rewrite
#                   db.child("movement_list").set(movement_list, user['idToken'])
                
                movement_list = []
            sleep(0.3)
            
GPIO.cleanup()

# Write to database once the OK button is pressed

