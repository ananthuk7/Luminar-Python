class Book:
    #static variable::defined in class
    library_name="ABC Library"
    def details(self, book_name, author, pages):
        self.book_name = book_name
        self.author = author
        self.pages = pages

    def printVar(self):
        print(self.book_name)
        print(self.author)
        print(self.pages)
        print(Book.library_name)

book=Book()
book.details("abc","authername",544)
book.printVar()
book1=Book()
book1.details("ab","authername1",544)
book1.printVar()