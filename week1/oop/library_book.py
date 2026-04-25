class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
        self.checked_out_by = None

    def checkout(self, member_name):
        if self.is_checked_out:
            print(f"'{self.title}' is unavailable — currently borrowed by {self.checked_out_by}.")
        else:
            self.is_checked_out = True
            self.checked_out_by = member_name
            print(f"'{self.title}' checked out by {member_name}.")

    def return_book(self):
        self.is_checked_out = False
        self.checked_out_by = None
        print(f"'{self.title}' has been returned. Thanks!")

    def status(self):
        state = f"checked out by {self.checked_out_by}" if self.is_checked_out else "available"
        print(f"'{self.title}' by {self.author} — {state}.")


if __name__ == "__main__":
    book = Book("1984", "George Orwell")
    book.status()
    book.checkout("Oriol")
    book.checkout("Maria")
    book.return_book()
    book.status()

