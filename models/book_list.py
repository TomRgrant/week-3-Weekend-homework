from models.book import Book

book_1 = Book("Harry Potter", "J.K. Rowling", "Fantasy")
book_2 = Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy")
book_3 = Book("Kensuke's Kingdom", "Michael Morpurgo", "Fantasy")

book_3.checked_out = True

book_list = [book_1, book_2, book_3]

def get_book_list():
    return book_list

def add_new_book(new_book):
    book_list.append(new_book)

def delete_book(index):
    book_list.pop(index)