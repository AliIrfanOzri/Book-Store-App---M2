import json

'''
Concerensed with stroring and retriving book from a json file.

format :
[
  {
  "name":"Clean Code"
  "auther":"Martin"
  "read":True
  }
]

'''



books_file= "books.json"


# "with" = context manager


def create_table():
    with open(books_file,'w') as file:
        json.dump([],file)



def add_book(name, aouther):
    books = get_all_books()
    books.append({'name':name,'aouther':aouther,'read':False})
    _save_all_books(books)


def get_all_books():
    with open(books_file,'r') as file:
       return json.load(file) # it give is (as format define Above in File)


def _save_all_books(books):
    with open(books_file,'w') as file:
        json.dump(books,file) # save data is json string


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read']= True
    _save_all_books(books)





def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

