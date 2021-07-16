# create a book program


# find book
# book name number of copies
# sort author names based on sold data


# def find_book(func):
#     def wrapper(self, book_name, *args, **kwargs):
#         if book_name in self.books:
#             func(self, book_name, *args, **kwargs)
#         else:
#             print("not available")
#
#     return wrapper


class Book:
    books = {
        "alchemist": {"book_name": "alchemist", "author": "paulo", "price": "200", "av_copies": 100},
        "hgf": {"book_name": "hgf", "author": "heathen", "price": "100", "av_copies": 200},
        "xyz": {"book_name": "Balch", "author": "paul", "price": "300", "av_copies": 0}
    }

    # @find_book
    # def av_copies(self, book_name):
    #     copy=self.books[book_name]["av_copies"]
    #     if copy != 0:
    #         print(copy)
    #         return copy
    #     else:
    #         print("book not available")
    #     return copy
    def all_book_details(self):
        for book_name in self.books:
            bkname = self.books[book_name]["book_name"]
            author = self.books[book_name]["author"]
            price = self.books[book_name]["price"]
            av_stock = self.books[book_name]["av_copies"]
            print(f"book name : {bkname} author : {author} price : {price} available copies : {av_stock}")

    def book_available(self, book_name):
        if book_name in self.books:
            return True
        else:
            return False

    def book_details(self, book_name):
        available = self.book_available(book_name)
        if available:
            print("book name", self.books[book_name]["book_name"])
            print("author", self.books[book_name]["author"])
            print("price", self.books[book_name]["price"])
            print("available copies", self.books[book_name]["av_copies"])
        else:
            print(f"The {book_name} not available here")

    def buy_book(self, **kwargs):
        book_name = kwargs["book_name"]
        no_of_copies = kwargs["no_of_copies"]

        available = self.book_available(book_name)
        if available:
            if self.books[book_name]["av_copies"] != 0:
                if no_of_copies > self.books[book_name]["av_copies"]:
                    var = self.books[book_name]["av_copies"]
                    print(f"our stock have only {var} left")
                else:
                    self.books[book_name]["av_copies"] -= no_of_copies
            else:
                print("out of stock")

    av_stock = []

    def author(self):
        author = []
        for book_name in self.books:
            if self.books[book_name]["av_copies"] != 0:
                self.av_stock.append(self.books[book_name]["av_copies"])
        self.av_stock.sort(reverse=True)
        for stock in self.av_stock:
            for book_name in self.books:
                if self.books[book_name]["av_copies"] == stock:
                    value = self.books[book_name]["author"]
                    author.append(value)
                    break
        print(author)

    def add_book(self, **kwargs):
        book = kwargs["book"]
        book_name = kwargs["book_name"]
        author = kwargs["author"]
        price = kwargs["price"]
        av_stock = kwargs["av_stocks"]
        self.books[book] = {"book_name": book_name, "author": author, "price": price, "av_copies": av_stock}

    def stock_update(self, book_name, copies):
        self.books[book_name]["av_copies"] += copies

    def remove_book(self, book_name):
        del self.books[book_name]

# obj1=Book()
# obj1.all_book_details()
# obj1.book_details("alchemist")
# obj1.remove_book("alchemist")
# obj1.book_details("alchemist")
# obj1.buy_book(book_name="alchemist",no_of_copies=10)
# obj1.book_details("alchemist")
# obj1.author()
# obj1.add_book(book="abc", book_name="abc",author="ctc",price="100",av_stocks=150)
# var=obj1.books
# print(var)
# obj1.stock_update("alchemist",100)
# obj1.book_details("alchemist")


# obj = Book()
# val=obj.av_copies("hgf")
# print(val)
# obj.buy_books("hgf")

obj = Book()
while True:
    print("<====BOOK MANAGEMENT ====>")
    print("1.View All Book Available")
    print("2.Book Details")
    print("3. Add Book")
    print("4. Update stock")
    print("5. Remove Book")
    print("6. author name based stock availability")
    print("7. exit")
    ch = int(input("enter what you want to perform"))
    if ch == 1:
        obj.all_book_details()
    elif ch == 2:
        book = input("which book details you want")
        obj.book_details(book)
    elif ch == 3:
        book_name = input("enter the name of the book")
        author = input("author name")
        price = input("price of book")
        stock = int(input("number of stock"))
        obj.add_book(book=book_name, book_name=book_name, author=author, price=price, av_stocks=stock)
    elif ch == 4:
        book = input("enter the name of book")
        stock = int(input("enter the number of copies you want to added"))
        obj.stock_update(book, stock)
    elif ch == 5:
        book = input("enter the name of book u want to delete")
        obj.remove_book(book)
    elif ch == 6:
        obj.author()
    else:
        break
#


