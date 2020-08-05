import mysql.connector as mysql

#   Start mysql
db = mysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='lifechoicesonline'    # Uses the db lifechoicesonline.

)

cursor = db.cursor()

# Creates tables in case of errors or want to clear the tables of data.
try:
    # Creates the table users which contains the details of all registered users.
    cursor.execute("drop table if exists user_log;")
    cursor.execute("drop table users;")
    cursor.execute("create table users(id int(11) NOT NULL AUTO_INCREMENT, full_name varchar(60) NOT NULL ,"
                   "username varchar(50)NOT NULL UNIQUE, password varchar(20) NOT NULL,"
                   " cell_number varchar(10) NOT NULL, "
                   "PRIMARY KEY(id));")
    cursor.execute("describe users")
    cursor.fetchall()
    print("Table successfully added")
except:
    print("Table users already exists")

try:
    # Creates the login and logout table.
    cursor.execute("create table user_log(id int(11) NOT NULL, full_name varchar(60) NOT NULL ,"
                   "username varchar(50)NOT NULL, sign_in_time datetime not null, sign_out_time datetime null,"
                   "Foreign key(id) references users(id));")
    cursor.execute("describe user_log")
    e = cursor.fetchall()
    for i in e:
        print(i)
    print("Table successfully added")
except TypeError:
    print('TypeError occurred')
except EOFError:
    print("EOFError occurred")
except ValueError:
    print("Value error occurred")
except:
    print("Table sign_in already exists")


