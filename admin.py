from admin_mysql import AddUsersTable, DeleteUsersTable, log_table, User

# Create admin local host
# Create password and username
# Give privileges
# AddAndDelete adds and removes people
# Can see table for sign in and sign out


def admin_login():
    login = True
    unsuccessful_login = True

    while login:
        # check if username and password is correct.
        print("Administration Login Screen:")
        # username = admin
        username = input("Please enter username: " + "\n")
        # password = 1234
        password = input("Please enter password: " + "\n")
        if username == "admin" and password == "1234":
            print("\n" + "You have successfully logged in!" + "\n")

            logged_in = True
            while logged_in:
                # admin main menu
                admin_options = "Would you like to " + "\n"
                admin_options += " 1) Create a user account" + "\n"
                admin_options += " 2) Delete a user account" + "\n"
                admin_options += " 3) Upgrade user privileges." + "\n"
                admin_options += " 4) Downgrade user privileges." + "\n"
                admin_options += " 5) View logon events" + "\n"
                admin_options += " 6) Exit" + "\n"
                print(admin_options)
                options = int(input("Choose option (1, 2, 3, 4, 5 or 6):"))

                # option 1 - creating a new user account
                if options == 1:
                    fullname = input("Please enter new fullname: ")
                    user = input("Please enter new username: ")
                    passwd = input("Please enter new password: ")
                    cell_number = input("Please enter new cell_number: ")
                    ObjAddUser = AddUsersTable(fullname, user, passwd, cell_number)
                    ObjAddUser.add_user()
                    objCreateUser = User(fullname, user, passwd, cell_number)
                    objCreateUser.create_user()
                    logged_in = True

                # option 2 - deleting a user account
                elif options == 2:
                    fullname = None
                    passwd = None
                    cell_number = None
                    user = input("Please enter username: ")
                    ObjDeleteUser = DeleteUsersTable(fullname, user, passwd, cell_number)
                    ObjDeleteUser.delete_user()
                    objDropUser = User(fullname, user, passwd, cell_number)
                    objDropUser.drop_user()

                # option 3 - upgrade user privileges
                elif options == 3:
                    fullname = None
                    passwd = None
                    cell_number = None
                    user = input("Please enter username: ")
                    objgrant = User(fullname, user, passwd, cell_number)
                    objgrant.upgrade_user_privilege()

                # option 4 - downgrading user privileges
                elif options == 4:
                    fullname = None
                    passwd = None
                    cell_number = None
                    user = input("Please enter username: ")
                    objdemote = User(fullname, user, passwd, cell_number)
                    objdemote.downgrade_user_privileges()

                # option 1 - view who logged in and out
                elif options == 5:
                    log_table()

                # option 1 - exit programme
                elif options == 6:
                    print("Goodbye :D")
                    exit()

                # main menu loop continues
                else:
                    pass

        else:
            login_unsuccessful = "\n" + "Login was unsuccessful!" + "\n"
            login_unsuccessful += "\n" + "Would you like to:" + "\n"
            login_unsuccessful += " 1) Go back to the main menu" + "\n"
            login_unsuccessful += " 2) Try again" + "\n"
            login_unsuccessful += " 3) Exit" + "\n"
            print(login_unsuccessful)
            login = False

    login_unsuccessful_options = int(input("Please choose option (1,2 or 3):"))

    # login unsuccessful menu
    while unsuccessful_login:
        if login_unsuccessful_options == 1:
            # Go back to main menu
            unsuccessful_login = False
        elif login_unsuccessful_options == 2:
            # Try to login again
            admin_login()
        elif login_unsuccessful_options == 3:
            # exit programme
            print("Goodbye :)")
            exit()
        else:
            exit()
