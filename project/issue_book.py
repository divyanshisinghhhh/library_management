from utils import books, issue_books

def issue():
    book_name = input("Enter book name: ").upper()
    if book_name in books:
        books.remove(book_name)
        issue_books.append(book_name)
        print("Book assigned successfully")
    else:
        print("Book not available")