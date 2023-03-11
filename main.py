import pymysql

from sql_commands import create_tables, insert_values

if __name__ == "__main__":

    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='alternance',
    cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()  

    # create_tables(False, cursor)
    insert_values(cursor)

    connection.commit()
    connection.close()