'''
Concerensed with stroring and retriving book from list.
(immemory data base)
'''

books = []


def add_book(name, aouther):
    books.append({'name':name, 'aouther':aouther, "read":False})


def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read']=True
            break

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]

