class Publisher:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("The title is : ", self.title)
        print("The author is : ", self.author)


class Book(Publisher):
    def __init__(self, title, author, price, no_of_pages):
        self.price = price
        self.no_of_pages = no_of_pages
        super().__init__(title, author)

    def display(self):
        print()
        super().display()
        print("The price is : ", self.price)
        print("The no of pages is : ", self.no_of_pages)


a = input("Enter the title: ")
b = input("Enter the author: ")
c = int(input("Enter the price: "))
d = int(input("Enter the number of pages: "))
b1 = Book(a, b, c, d)
b1.display()
