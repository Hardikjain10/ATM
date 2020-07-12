import getpass
import time


def statements():
    if username == "superman":
        amounts = 76534.24
    elif username == "batman":
        amounts = 32832.27
    elif username == "ironman":
        amounts = 72638.16
    response = input(
        "select from the following options:\n 1.statements \n 2.withdrawal \n 3.Deposit \n 4.change of pin \n 5.Quit \n ")
    valid__responses = ["1", "2", "3", "4", "5"]
    if response == "1":
        print("Name: ", str.capitalize(username), "\nAvailable balance : $", amounts)
        statements()
    elif response == "2":
        withdrawal = int(input("enter amount for withdrawal: "))
        if withdrawal % 10 != 0:
            print("Amount must be in multiple of 500 or 100")
        elif withdrawal > amounts:
            print("insufficent balance")
        else:
            amounts = amounts - withdrawal
            print(f"available balance: ${amounts}")
            statements()
    elif response == "3":
        deposit = int(input("enter the amount to deposit: "))
        if deposit % 10 != 0:
            print("deposit should be multiple of 100 or 500 or 1000")
        else:
            amounts = amounts + deposit
            print(f"available balance: ${amounts}")
            statements()
    elif response == "4":
        new_pin = str(getpass.getpass("enter new pin"))
        if new_pin.isdigit() and new_pin != user[username] and len(new_pin) == 4:
            new_ppin = str(getpass.getpass("Confirm pin"))
            if new_ppin != new_pin:
                print("pin mismatch!")
            else:
                print("pin saved")
                statements()
        else:
            print("new pin must consist of 4 digits and must be different from previous pin ")
    elif response == "5":
        print('Thank you! Visit Again')
        exit()
    else:
        print("Invalid response")


complete = False
user = {"superman": "1234", "batman": "3333", "ironman": "4321"}
chances = 0

while not complete and chances < 3:
    print('CAUTION:You get only three chances,If failed the Card get Blocked.')
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username == user and password == password:
        continue
    elif username not in user:
        print('Connecting to server...........')
        time.sleep(3)
        print("This is not a valid username, input username again!")
        chances += 1
        print(f'{3 - chances}left')
    elif password != user[username]:
        print('Connecting to server...........')
        time.sleep(3)
        print(f"Password is not valid for {username}. ")
        chances += 1
        print(f'{3 - chances}left')
    elif password == user[username]:
        print('Connecting to server...........')
        time.sleep(3)
        print("Username and Password Validated successful")
        print(f"\nWelcome {username} ")
        print(f"\nWelcome to DCMarvel Bank ATM. ")
        chances = 3
        complete = True
        statements()
        break

else:
    print('Card Blocked')
