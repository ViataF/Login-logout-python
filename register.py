import mysql.connector as mysql

#   Start mysql
db = mysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='lifechoicesonline'
)
# cursor in order to use the mysql functions
cursor = db.cursor()

# Option 1 in the main menu (register user)


def registration(full_name, username, password, cell_number):
    """
    >>> registration("viata fredericks","vf" ,"1234", "12345678")
    (33, 'viata fredericks', 'vf', '1234', '12345678')
    You have registered successfully
    """
    try:
        # Inserts values into the certain rows of the user table.
        query = "insert into users(full_name, username, password,cell_number) values(%s,%s,%s,%s)"
        values = (full_name, username, password, cell_number)
        cursor.execute(query, values)
        db.commit()

        # Once user is created user is able to see their details
        query2 = "select * from users where username = %s;"
        value2 = (username,)
        cursor.execute(query2, value2)
        records = cursor.fetchall()
        for record in records:
            print(record)
        print("You have registered successfully")
    except TypeError:
        print('TypeError occurred')
    except EOFError:
        print("EOFError occurred")
    except ValueError:
        print("Value error occurred")
    except:
        # if username is already in use or cell number too long,
        # the following error message will appear and it will go back to main menu.
        registration_unsuccessful = "Registration was unsuccessful!" + "\n"
        registration_unsuccessful += "Username is already in use or invalid cellphone number. " + "\n"
        print(registration_unsuccessful)

def registration_input():
    # Inputs the users details and calls registration function.
    create_full_name = input("Please enter your fullname:")
    create_username = input("Please create a new username:")
    create_password = input("Please create a new password:")
    cell_phone_number = input("Please enter your cellphone number:")

    # if the fields are left blank then registration will loop over again.
    if create_full_name == "" or create_username == "" or create_password == "" or cell_phone_number == "":
        print("\n Please fill in the fields")
        registration_input()
        print()
    else:
        registration(create_full_name, create_username, create_password, cell_phone_number)

