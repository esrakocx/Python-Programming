import sqlite3
import time


class Book():

    def __init__(self, name, writer, publisher, kind, edition):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.kind = kind
        self.edition = edition

    def __str__(self):
        return "Name: {}\nWriter: {}\nPublisher: {}\nKind: {}\nEdition: {}".format(self.name, self.writer, self.publisher, self.kind, self.edition)


class Library():

    def __init__(self):
        self.creat_con()

    def creat_con(self):
        self.con = sqlite3.connect("library.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Bookcase (Name TEXT, Writer TEXT, Publisher TEXT, Kind TEXT, Edition INT)")
        self.con.commit()

    def disconnect(self):
        self.con.close()

    def show_books(self):
        self.cursor.execute("SELECT * FROM Bookcase")
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no any book..!")
        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def query_book(self, name):
        self.cursor.execute("SELECT * FROM Bookcase where name = ?", (name,))
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no book you are looking for..!")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            print(book)

    def add_book(self, book):
        self.cursor.execute("INSERT INTO Bookcase VALUES (?,?,?,?,?)", (book.name, book.writer, book.publisher, book.kind, book.edition))
        self.con.commit()

    def delete_book(self, name):
        self.cursor.execute("DELETE FROM Bookcase WHERE Name = ?", (name,))
        self.con.commit()

    def raise_edition(self, name):
        self.cursor.execute("SELECT * FROM Bookcase WHERE Name = ?", (name,))
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no book you are looking for..!")
        else:
            edition = books[0][4]
            edition += 1

            self.cursor.execute("UPDATE Bookcase set Edition = ? WHERE Name = ?", (edition, name))
            self.con.commit()






