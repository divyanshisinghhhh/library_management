from utils import books

def add():
    book_name = input("Enter the Book name to add: ").upper()
    books.append(book_name)
    print(f"Book Added: {book_name}")
    