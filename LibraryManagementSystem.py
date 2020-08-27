class Library():

    def __init__(self, list_of_books, library_name):
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name

        for books in self.list_of_books:
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}.{books}")

    def lend_books(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = author
            else:
                print(f"Sorry this book is lended by {self.lend_data[book]}")
        else:
            print("No such book is available")

    def return_books(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("The book is not lended")

        else:
            print("No such book is available")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def remove_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)


def main():
    list1 = ["JKRowling", "HarryPotter", "The control of mind"]
    library_name = "MEHUL LIBRARY"
    pincode = 12345

    Mehul = Library(list1, library_name)

    print(f"Welcome to {Mehul.library_name}")
    print("1.Display\n2.Lend\n3.Return\n4.Add\n5.Remove\n6.Exit")

    Exit = False
    while (Exit is not True):
        i = int(input("Enter your choice : "))

        if i == 1:
            print("--Displaying The Books---")
            print(Mehul.display_books())

        elif i == 2:
            input1 = str(input("Enter the book name : "))
            input2 = str(input("Enter your name :"))
            print("--Lending The Book---")
            print(Mehul.lend_books(input1, input2))

        elif i == 3:
            input3 = str(input("Enter the book name : "))
            input4 = str(input("Enter your name :"))
            print("--Returning the Book--")
            print(Mehul.return_books(input3, input4))

        elif i == 4:
            print("IN ORDER TO ADD BOOK YOU MUST INPUT CORRECT PIN")
            pin1 = int(input("Enter the pincode : "))

            if (pin1 == pincode):
                input5 = str(input("Enter the book name to add : "))
                print("---Adding the Book---")
                print(Mehul.add_book(input5))
            else:
                print("Invalid Pin")

        elif i == 5:
            print("IN ORDER TO REMOVE BOOK YOU MUST INPUT CORRECT PIN")
            pin2 = int(input("Enter the pincode : "))

            if (pin2 == pincode):
                input6 = str(input("Enter the book name to remove : "))
                print("---Removing the Book---")
                print(Mehul.remove_book(input6))
            else:
                print("Invalid Pin")

        elif i == 6:
            Exit = True

        else:
            print("Input correct value from 1 to 6")


if __name__ == '__main__':
    main()
