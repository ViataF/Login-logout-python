import mysql.connector as mysql
import datetime
from login_out import Login
#   Start mysql
db = mysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='lifechoicesonline'
)
cursor = db.cursor()


def sign_in_input():
    # user inputs their name and password so they can sign in
    username = (input("Please enter your username:"))
    password = input("Please enter your password:")
    date = datetime.datetime.now()
    # sign in function
    ObjSignin = Login(username, password, date)
    ObjSignin.sign_in()

    error_message = "Username or password is incorrect! Login was unsuccessful." + "\n"
    error_message += "Would you like to: " + '\n'
    error_message += " 1)Try again" + "\n"
    error_message += " 2) Go back to the main menu?" + "\n"
    print(error_message)

    # Option to try again or return to main menu if login is unsuccessful.
    options = (input("Please enter option(1 or 2)"))
    if options == '1':
        sign_in_input()
    elif options == '2':
        pass
    else:
        print("You have not chosen a valid answer! System will automatically exit")
        exit()
