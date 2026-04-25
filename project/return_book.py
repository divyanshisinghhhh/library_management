from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issue_books:
        issue_books.remove(book_name)
        books.append(book_name)
        print("Book returned")
    else:
        print("blablabla")