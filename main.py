# Viata Fredericks - Class 1
import admin
import register
from logs import sign_in_input
import datetime
from login_out import Logout

'''
What this project does:
1. Register user details.
2. Ability to sign-in and sign-out.
3. Upgrade/downgrade user privileges.
4. Show people who have signed-in for the day.
5. Show people who have signed-out for the day.
6. AddAndDelete add and remove users in the system.
'''

user = True


#   (Consider this the main screen)

def main():
    while user:
        #   displays the login screen with the option for new registration.
        #   This is the case when new employees or visitors arrive at the premises and would like to enter the building.

        log_screen = "Welcome to Life Choices Academy" + "\n"
        log_screen += "What would you like to do:" + "\n"
        log_screen += "1) Register as new user" + "\n"
        log_screen += "2) User Login" + "\n"
        log_screen += "3) User Logout" + "\n"
        print(log_screen)
        option1 = (input("Choose option (1, 2 or 3):"))

        #  Option 1 - Registers new user that enters the building.
        if option1 == '1':
            #  User adds in their details
            register_message = "Welcome to Life Choices Online!" + "\n"
            register_message += "Please fill in a few details to register with Life Choices Online."
            print(register_message)
            register.registration_input()

        # Option 2 - Login option if user already has an account.
        elif option1 == '2':
            # If the login option is clicked (selected), the user should be presented with the option
            # asking them to enter their full_name, username and password
            sign_in_input()

        # Option 3 - Logout option if user already logged in.
        elif option1 == '3':
            password = None
            full_name = None
            date = datetime.datetime.now()
            username = input("Please enter your username:")
            # OOP Logout of system and exit.
            ObjSignout = Logout(username, password, date, full_name)
            ObjSignout.sign_out()
            print("User not found in database!" + "\n")

        # Secret option - Admin log in
        elif option1 == 'a':  
            # When you are on the main screen, by pressing the “a” key, for admin,
            # you should be presented with a new screen to login.
            admin.admin_login()
            # username = admin
            # password = 1234


if __name__ == '__main__':
    main()
