from .database_connection import DatabaseConnection

'''
Concerensed with stroring and retriving book from a database.

'''


# "with" = context manager

DB = 'data.db'

def create_table():
   with DatabaseConnection(DB) as connection:
       cursor = connection.cursor()

    # cursor.execute('CREATE TABLE books(name text primary key,aouther text, read integer)')
       cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,aouther text, read integer)')



def add_book(name, aouther):
    with DatabaseConnection(DB) as connection:

       cursor = connection.cursor()

       # this not a recommended approch [auther = ",0);DROP TABLE] Eg OF SQL INGECTION
       # cursor.execute(f'INSERT INTO books VALUES("{name}","{aouther}",0)')

       #THIS FROMAT SAVE FROM SQL ATTACK. [this must be a tuple (name,aouther) ]
       cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,aouther))


def get_all_books():
    with DatabaseConnection(DB) as connection:
        cursor = connection.cursor()

        # coursor are pointer start from top of table
        cursor.execute('SELECT * FROM books')
        #fetchall
        #fetchmany
        #fetchone
        # books = cursor.fetchall() # it give us list of tuple [(name, aouther, read), (name, aouther, read)]

        #for our implimented code in book Store not effect convert in to Dect
        books = [{'name':row[0], 'aouther':row[1], 'read':row[2]} for row in cursor.fetchall()]

    # we not written any thing our database in this query thats why not use commit
    # connection.commit()
    # connection.close()

        return books


def mark_book_as_read(name):
    with DatabaseConnection(DB) as connection:
        cursor = connection.cursor()

        # this not a recommended approch [auther = ",0);DROP TABLE] Eg OF SQL INGECTION
        # cursor.execute(f'INSERT INTO books VALUES("{name}","{aouther}",0)')

        #THIS FROMAT SAVE FROM SQL ATTACK. [this must be a tuple (name,aouther) ]
        cursor.execute('UPDATE books set read=1 WHERE name=?',(name,))


def delete_book(name):
    with DatabaseConnection(DB) as connection:
        cursor = connection.cursor()

        # this not a recommended approch [auther = ",0);DROP TABLE] Eg OF SQL INGECTION
        # cursor.execute(f'INSERT INTO books VALUES("{name}","{aouther}",0)')

        #THIS FROMAT SAVE FROM SQL ATTACK. [this must be a tuple (name,aouther) ]
        cursor.execute('DELETE FROM books WHERE name=?',(name,))


