from Library import *

print("""*********************************

Welcome to the Library Program

Operations;

1. Show the Books

2. Query a Book

3. Add a Book

4. Delete a Book

5. Raise Edition

To exit please enter 'q'

*********************************""")

library = Library()

while True:
    choice = input("Your choice: ")

    if choice == "q":
        print("Program is terminated...")
        time.sleep(2)
        break

    elif choice == "1":
        library.show_books()

    elif choice == "2":
        name = input("Please enter a book name you want to query: ")
        print("The book is queried...")
        time.sleep(2)
        library.query_book(name)

    elif choice == "3":
        name = input("Book's Name: ")
        writer = input("Writer's Name: ")
        publisher = input("Publisher's Name: ")
        kind = input("Book's Kind: ")
        edition = int(input("Book's Edition: "))

        print("The book is almost added...")
        time.sleep(2)
        library.add_book(Book(name, writer, publisher, kind, edition))
        print("The book was added!")

    elif choice == "4":
        name = input("Please enter the book's name you want to delete: ")
        response = input("Are you sure you want to delete? Y/N : ")

        if response == "Y":
            print("The book is almost deleted...")
            time.sleep(1)
            library.delete_book(name)
            print("The book was deleted!")

    elif choice == "5":
        name = input("Please enter the book's name you want to raise its edition: ")
        print("The edition is raised...")
        time.sleep(2)
        library.raise_edition(name)
        print("The edition was updated!")

    else:
        print("Incorrect input!")
