import mysql.connector as mysql

admin_db = mysql.connect(
    host='localhost',
    user="admin",
    password='1234',
    database='lifechoicesonline'
)
cursor = admin_db.cursor()

# Admin login options
class AddAndDelete:
    def __init__(self, fullname, username, password, cell_number):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.cell_number = cell_number


class AddUsersTable(AddAndDelete):
    def add_user(self):
        try:
            # adding user to users table
            query = "insert into users(full_name, username, password,cell_number) values(%s,%s,%s,%s)"
            values = (self.fullname, self.username, self.password, self.cell_number)
            cursor.execute(query, values,)
            admin_db.commit()
            print("\nYou have successfully created a user account:"+"\n")
        except:
            error_message = "Failed To Add The User. "+'\n'
            error_message += "Username is already in use or cellphone number is invalid" + '\n'
            print(error_message)


class DeleteUsersTable(AddAndDelete):
    def delete_user(self):
        # delete user from login table
        query1 = "DELETE FROM user_log where username = %s"
        values1 = (self.username,)
        cursor.execute(query1, values1)

        # delete user from the user table
        query = "DELETE FROM users WHERE username = %s"
        values = (self.username,)
        cursor.execute(query, values, )
        admin_db.commit()
        print(cursor.rowcount, "record(s) deleted")


class User(AddAndDelete):
    def create_user(self):
        try:
            # create a user and give access to lifechoicesonline database
            query = "CREATE user %s @'localhost' identified by %s default role administrator;"
            values = (self.username, self.password,)
            cursor.execute(query, values)
            admin_db.commit()

        except:
            print("Username already exists!")

    def drop_user(self):
        try:
            # Delete user from lifechoicesonline database:
            query = "DROP user %s @'localhost'"
            values = (self.username,)
            cursor.execute(query, values)
            admin_db.commit()
            print("User " + self.username + " was deleted")
            print()

        except:
            # deletion unsuccessful fetch all users from database.
            print("Deletion of user was unsuccessful!")
            query = "SELECT HOST, USER FROM mysql.user;"
            cursor.execute(query)
            users = cursor.fetchall()
            for u in users:
                print(u)

    def downgrade_user_privileges(self):
        try:
            # downgrade privileges to read only
            query = "REVOKE 'administrator' FROM %s@'localhost';"
            query2 = "GRANT 'read_only' TO %s@'localhost';"
            value = (self.username,)
            cursor.execute(query, value)
            cursor.execute(query2, value)
            query3 = 'Flush privileges;'
            cursor.execute(query3)
            print("Downgrading user privilege was successful!" + "\n")
        except:
            print("Downgrading user privilege was unsuccessful! " + "\n")

    def upgrade_user_privilege(self):
        try:
            # upgrade user to administrator has access to lifechoicesonline
            query2 = "GRANT 'administrator' TO %s@'localhost';"
            value = (self.username,)
            cursor.execute(query2, value)
            query3 = 'Flush privileges;'
            cursor.execute(query3)
            print("Upgrading user privilege was successful! " + "\n")
        except:
            print("Upgrading user privilege was unsuccessful! " + "\n")

def log_table():
    try:
        # see the login and logout table
        sql = "select * from user_log;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        print("User sign_in and sign_out events" + "\n")
        for x in myresult:
            print(x)
    except:
        print("Log is empty!")
