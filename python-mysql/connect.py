import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

TABLES = {}
DB_NAME = "company"

TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    " `emp_no` int(10) NOT NULL AUTO_INCREMENT,"
    " `name` varchar(16) NOT NULL,"
    " PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB"
)

cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} create successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else: 
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name))
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else: print("OK")

cursor.close()
cnx.close()