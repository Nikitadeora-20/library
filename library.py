import json 

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def dict(self):
        return {"title":self.title, "author":self.author , "isbn":self.isbn}

class User:
    def __init__(self, username, userid):
        self.username = username
        self.userid = userid

class Library:
    def __init__(self, filename ="data.json"):
        self.filename = filename
        self.books = self.load_books()


    def load_books(self):
        
        try:
            with open(self.filename, "r") as file:
                return [Book(**book) for book in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        
        with open(self.filename, "w") as file:
            json.dump([book.dict() for book in self.books], file, indent=4)
            print("save books ")

       

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        print(f'Book "{title}" added successfully!')

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                print(f'Book "{book.title}" removed successfully!')
                return
        print("Book not found!")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f'Book Found: "{book.title}" by {book.author}, ISBN: {book.isbn}')
                return book
        print("Book not found.")

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                print(f'Book "{book.title}" has been issued.')
                return
        print("Book not available!")

    def return_book(self, title, author, isbn):
        returned_book = Book(title, author, isbn)
        self.books.append(returned_book)
        self.save_books()
        print(f'Book "{title}" has been returned.')

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Available Books:")
        for book in self.books:
            print(f' - {book.title} by {book.author}, ISBN: {book.isbn}')

if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary System Management")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Display Books")
        print("7. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)

        elif user_choice == "2":
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)

        elif user_choice == "3":
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif user_choice == "4":
            isbn = input("Enter book ISBN to issue: ")
            library.issue_book(isbn)

        elif user_choice == "5":
            title = input("Enter book title to return: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.return_book(title, author, isbn)

        elif user_choice == "6":
            library.display_books()

        elif user_choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")