import mysql.connector as mysql

#   Start mysql
db = mysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='lifechoicesonline'
)
cursor = db.cursor()

"""If the login option is clicked (selected), the user should be presented with the option
asking them to enter their full_name, username and password.

Populates the database table to keep track of who has logged-in or logged-out of the system.
"""


class LoginScreen:
    def __init__(self, username, password, date_time):
        self.username = username
        self.password = password
        self.date_time = date_time


class Login(LoginScreen):

    def sign_in(self):
        # if full_name and password is found in table insert id and username,full_name and time into table user login
        # selecting all user names in users and checking if the user input is in the list;
        cursor.execute("select username from users;")
        get_usernames = cursor.fetchall()
        for usernames_list in get_usernames:
            if self.username in usernames_list:
                cursor.execute("select password from users;")
                get_password = cursor.fetchall()

                # if the user password is in the list of passwords then select the users full_name;
                for password_list in get_password:
                    if self.password in password_list:
                        answer = "select full_name from users where username = %s"
                        value = (self.username,)
                        cursor.execute(answer, value)
                        myresult = cursor.fetchall()

                        # Get the username an password from users.
                        for x in myresult:
                            for y in x:
                                answer = "select id from users where username = %s"
                                value = (self.username,)
                                cursor.execute(answer, value)
                                result = cursor.fetchall()

                                # Insert the username, id, full_name and time into user_log table.
                                # User has signed in
                                for user_id in result:
                                    for i in user_id:
                                        query = "insert into user_log(id,username,full_name,sign_in_time) " \
                                                "values(%s,%s,%s,%s)"
                                        values = (i, self.username, y, self.date_time,)
                                        cursor.execute(query, values)
                                        db.commit()
                                        login_successful = "Login Successful! Enjoy Your Day :)" + "\n"
                                        print(login_successful)
                                        exit()


class Logout(LoginScreen):
    def __init__(self, password, username, date_time, full_name):
        super().__init__(username, password, date_time)
        self.full_name = full_name

    def sign_out(self):
        # user logout of the system
        # if username, full_name and password is found in table insert id and username time now into table user logout
        cursor.execute("select username from user_log;")
        get_username = cursor.fetchall()
        for names in get_username:
            if self.full_name in names:
                sql = "UPDATE user_log SET sign_out_time = %s WHERE username = %s"
                values = [self.date_time, self.username]
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record(s) affected")
                print("You have successfully signed out! Enjoy the rest of your day.\nBye...")
                exit()
