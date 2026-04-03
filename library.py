class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False   # default state
    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book issued")
        else:
            print("Already issued")
    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print("Book returned")
        else:
            print("Book was not issued")
book1 = Book("Python Basics", "John")
book1.issue_book()     # Book issued
book1.issue_book()     # Already issued
book1.return_book()    # Book returned
book1.return_book()    # Book was not issued