from libdw import pyrebase
import random

def init_firebase():
    # Create a firebase object by specifying the URL of the database and its secret token.
    # The firebase object has functions put and get, that allows user to put data onto
    # the database and also retrieve data from the database.
    from credential import *

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()
    user = auth.sign_in_with_email_and_password(email, password)

    return db, user

# CODE BELOW WILL GENERATE RANDOM VALUES AND FILL UP THE FIREBASE LIST
def generate_random_bin_values(db, user, no_of_bins):
    # Takes in a firebase database, generates randomly values for Bins 1 to 5 and uploads to Firebase
    myBins = {}
    binNames = []
    # Create dictionary of bins and list of binNames to access the Dict
    for i in range(1, no_of_bins + 1):
        name = 'Bin' + str(i)
        binNames.append(name)
        myBins[name] = {'Smell': random.randint(0, 1), 'Ultrasonic': random.randint(0, 1), 'Water': random.randint(0, 1)}

    for i in binNames:
        for log_no in range(3):
            log_string = f"{random.randint(1, 7)} {random.randint(0, 23)} {random.randint(0, 59)} {random.randint(0, 1)}"
            db.child('log').child(i).push(log_string)


    db.child('current_bin_states').update(myBins)
    

def read_bin_log_values(db, user):
    # Takes in a Firebase Database and user token, returns bin_states and log as ordered dictionaries
    bin_states = db.child('current_bin_states').get(user['idToken'])
    log = db.child('log').get(user['idToken'])

    # print(bin_states.val())
    # print(log.val())

    return bin_states.val(), log.val()

def update_specific_bin_state(db, user, update_list, bin_name):
    # Takes in a Firebase Database, user, and update_list string and updates the specific Firebase child node, and returns updated list values in a string
    output = f"Smell: {update_list[1]}, Ultrasonic: {update_list[4]}, Water: {update_list[7]}\n"

    bin_state_dict = {'Smell': int(update_list[1]), 'Ultrasonic': int(update_list[4]), 'Water': int(update_list[7])}
    db.child('current_bin_states').child(bin_name).set(bin_state_dict)

    return output

def main():
    db, user = init_firebase() # Initialize Firebase Database
    bin_state_list = None
    log_state_list = None
    # Enter main loop to collect user input and execute functions
    while True:
        input_string = input("Enter 1 to Generate Random Values, Enter 2 to change Specific Bins, 3 to Exit Program:")
        if input_string == '1':
            # While loop to ensure correct input values from the user (Integer from 1 to 10)
            while True:
                no_of_bins = input("Enter no. of bins to be Generated (Between 1 to 10):")
                try:
                    no_of_bins = int(no_of_bins)
                    if no_of_bins >= 1 and no_of_bins <= 10:
                        break
                    else:
                        print("Value entered is not Valid! Try again")
                except ValueError:
                    print("Value entered is not Valid! Try again")

            # Run function to generate and update Firebase values
            generate_random_bin_values(db, user, no_of_bins)
            print("Values Successfully generated! Check Firebase for Updated Values\n")
        elif input_string == '2':
            bin_state_list, log_state_list = read_bin_log_values(db, user)
            # While loop to ensure correct input values from the user (String from BinList)
            while True:
                print(f"Current Available Bins: {bin_state_list}")
                bin_name = input("Enter Bin Number to be edited (Eg. 'Bin1', 'Bin2'): ")
                if bin_name in bin_state_list:
                    break
                else:
                    print("Value entered is not Valid! Try again\n")

            while True:
                print(f"\n{bin_name}'s current state is {bin_state_list[bin_name]}")
                input_list = input("Enter input configuration: (Eg. s0 u1 w1, s1 u0 w0, etc.): ")
                if len(input_list) != 8:
                    print("Value entered is not Valid! Try again")
                elif input_list[0] == 's' and input_list[3] == 'u' and input_list[6] == 'w':
                    ones_and_zeroes = ['0', '1']
                    if input_list[1] in ones_and_zeroes and input_list[4] in ones_and_zeroes and input_list[7] in ones_and_zeroes:
                        # Input is successful
                        break
                    else:
                        print("Value entered is not Valid! Try again")
                else:
                    print("Value entered is not Valid! Try again")

            output = update_specific_bin_state(db, user, input_list, bin_name)
            print(f"Successfully updated {bin_name}'s state to {output}")


        elif input_string == '3':
            break
        else:
            print("Invalid Input! Try again")

main()