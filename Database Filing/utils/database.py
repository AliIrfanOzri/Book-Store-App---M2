'''
Concerensed with stroring and retriving book from a cav file.
Format of csv file :

name,auther,read\n
'''

books_file= "books.txt"

def create_table():
    with open(books_file,'w'):
        pass


def add_book(name, aouther):
    with open(books_file,'a') as file:
         file.write(f'{name},{aouther},0\n')


def get_all_books():
    with open(books_file,'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    # line [[name,auther,read],[name,auther,read]]
    return [{'name':line[0],'aouther':line[1],'read':line[2]} for line  in lines]


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read']= '1'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file,'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['aouther']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

