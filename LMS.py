import tkinter as tk
from tkinter import messagebox

# This is a simple library management system that allows users to list, add, remove, and search books, as well as add
# and remove members. Users can also borrow and return books. The system uses text files to store book and member
# information, and borrowed books. The system is built using the tkinter library for the GUI.

# LibraryGUI class is the main class that creates the GUI for the library management system. It has methods for each
# action that can be performed in the system.
class LibraryGUI:
    """Class for the library management system GUI."""
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("200x250")

        self.label = tk.Label(master, text="*** MENU ***", font=("Arial", 20))
        self.label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        self.list_books_button = tk.Button(master, text="List Books", command=self.list_books)
        self.list_books_button.grid(row=1, column=0, sticky="ew", padx=5, pady=10)

        self.add_book_button = tk.Button(master, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=1, column=1, sticky="ew", padx=5, pady=10)

        self.remove_book_button = tk.Button(master, text="Remove Book", command=self.remove_book)
        self.remove_book_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.search_book_button = tk.Button(master, text="Search Book", command=self.search_book)
        self.search_book_button.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.add_member_button = tk.Button(master, text="Add Member", command=self.add_member)
        self.add_member_button.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.borrow_book_button = tk.Button(master, text="Borrow Book", command=self.borrow_book)
        self.borrow_book_button.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.give_back_book_button = tk.Button(master, text="Give Back Book", command=self.give_back_book)
        self.give_back_book_button.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        self.output_label = tk.Label(master, text="", font=("Arial", 12))
        self.output_label.grid(row=5, column=0, columnspan=2)

        self.library = Library()
        self.member_manager = MemberManager()

    def list_books(self):
        self.output_label.config(text="")
        books = self.library.list_books()
        if books:
            self.output_label.config(text=books)
        else:
            self.output_label.config(text="No books available.")

    def add_book(self):
        self.output_label.config(text="")
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Add Book")

        self.title_label = tk.Label(self.add_window, text="Title:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.add_window)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(self.add_window, text="Author:")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(self.add_window)
        self.author_entry.grid(row=1, column=1)

        self.release_label = tk.Label(self.add_window, text="Release Year:")
        self.release_label.grid(row=2, column=0)
        self.release_entry = tk.Entry(self.add_window)
        self.release_entry.grid(row=2, column=1)

        self.pages_label = tk.Label(self.add_window, text="Number of Pages:")
        self.pages_label.grid(row=3, column=0)
        self.pages_entry = tk.Entry(self.add_window)
        self.pages_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(self.add_window, text="Submit", command=self.submit_add_book)
        self.submit_button.grid(row=4, columnspan=2)

    def submit_add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        release_date = self.release_entry.get()
        pages = self.pages_entry.get()
        if title and author and release_date and pages:
            self.library.add_book(title, author, release_date, pages)
            self.add_window.destroy()
            self.output_label.config(text="Book added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def remove_book(self):
        self.output_label.config(text="")
        self.remove_window = tk.Toplevel(self.master)
        self.remove_window.title("Remove Book")

        self.title_label = tk.Label(self.remove_window, text="Title:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.remove_window)
        self.title_entry.grid(row=0, column=1)

        self.submit_button = tk.Button(self.remove_window, text="Submit", command=self.submit_remove_book)
        self.submit_button.grid(row=1, columnspan=2)

    def submit_remove_book(self):
        title = self.title_entry.get()
        if title:
            self.library.remove_book(title)
            self.remove_window.destroy()
            self.output_label.config(text="Book removed successfully!")
        else:
            messagebox.showerror("Error", "Please enter a title.")

    def search_book(self):
        self.output_label.config(text="")
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Search Book")

        self.search_label = tk.Label(self.search_window, text="Enter search keyword:")
        self.search_label.grid(row=0, column=0)
        self.search_entry = tk.Entry(self.search_window)
        self.search_entry.grid(row=0, column=1)

        self.submit_button = tk.Button(self.search_window, text="Search", command=self.submit_search_book)
        self.submit_button.grid(row=1, columnspan=2)

    def submit_search_book(self):
        keyword = self.search_entry.get()
        if keyword:
            search_result = self.library.search_book(keyword)
            if search_result:
                self.output_label.config(text=search_result)
            else:
                self.output_label.config(text="No matching books found.")
        else:
            messagebox.showerror("Error", "Please enter a search keyword.")

    def add_member(self):
        self.output_label.config(text="")
        self.add_member_window = tk.Toplevel(self.master)
        self.add_member_window.title("Add Member")

        self.name_label = tk.Label(self.add_member_window, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.add_member_window)
        self.name_entry.grid(row=0, column=1)

        self.id_label = tk.Label(self.add_member_window, text="ID:")
        self.id_label.grid(row=1, column=0)
        self.id_entry = tk.Entry(self.add_member_window)
        self.id_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.add_member_window, text="Submit", command=self.submit_add_member)
        self.submit_button.grid(row=2, columnspan=2)

    def submit_add_member(self):
        name = self.name_entry.get()
        member_id = self.id_entry.get()
        if name and member_id:
            self.member_manager.add_member(name, member_id)
            self.add_member_window.destroy()
            self.output_label.config(text="Member added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def borrow_book(self):
        self.output_label.config(text="")
        self.borrow_book_window = tk.Toplevel(self.master)
        self.borrow_book_window.title("Borrow Book")

        self.member_id_label = tk.Label(self.borrow_book_window, text="Member ID:")
        self.member_id_label.grid(row=0, column=0)
        self.member_id_entry = tk.Entry(self.borrow_book_window)
        self.member_id_entry.grid(row=0, column=1)

        self.book_title_label = tk.Label(self.borrow_book_window, text="Book Title:")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = tk.Entry(self.borrow_book_window)
        self.book_title_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.borrow_book_window, text="Submit", command=self.submit_borrow_book)
        self.submit_button.grid(row=2, columnspan=2)

    def submit_borrow_book(self):
        member_id = self.member_id_entry.get()
        book_title = self.book_title_entry.get()
        if member_id and book_title:
            success = self.library.borrow_book(member_id, book_title)
            if success:
                self.borrow_book_window.destroy()
                self.output_label.config(text="Book borrowed successfully!")
            else:
                messagebox.showerror("Error", "Book not available or member ID not found.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def give_back_book(self):
        self.output_label.config(text="")
        self.give_back_window = tk.Toplevel(self.master)
        self.give_back_window.title("Give Back Book")

        self.member_id_label = tk.Label(self.give_back_window, text="Member ID:")
        self.member_id_label.grid(row=0, column=0)
        self.member_id_entry = tk.Entry(self.give_back_window)
        self.member_id_entry.grid(row=0, column=1)

        self.book_title_label = tk.Label(self.give_back_window, text="Book Title:")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = tk.Entry(self.give_back_window)
        self.book_title_entry.grid(row=1, column=1)

        self.submit_button = tk.Button(self.give_back_window, text="Submit", command=self.submit_give_back_book)
        self.submit_button.grid(row=2, columnspan=2)

    def submit_give_back_book(self):
        member_id = self.member_id_entry.get()
        book_title = self.book_title_entry.get()
        if member_id and book_title:
            success = self.library.give_back_book(member_id, book_title)
            if success:
                self.give_back_window.destroy()
                self.output_label.config(text="Book returned successfully!")
            else:
                messagebox.showerror("Error", "Book not borrowed or member ID not found.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")


# Library class is the main class that handles the book management system. It has methods for listing, adding, removing,
# and searching books, as well as borrowing and returning books. It uses a text file to store book information and
# borrowed books.
class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        self.borrowed_books = {}

    def __del__(self):
        self.file.close()

    def list_books(self):
        # Reset file pointer to the beginning of the file and read all lines
        self.file.seek(0)
        books = self.file.read().splitlines()
        return "\n".join(books)

    def add_book(self, title, author, release_date, pages):
        book_info = f"{title},{author},{release_date},{pages}\n"
        self.file.write(book_info)

    def remove_book(self, title):
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        for book in books:
            if title not in book:
                new_books.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(new_books)

    def search_book(self, keyword):
        self.file.seek(0)
        books = self.file.read().splitlines()
        matching_books = []
        for book in books:
            if keyword.lower() in book.lower():
                matching_books.append(book)
        return "\n".join(matching_books)

    def borrow_book(self, member_id, book_title):
        if book_title in self.borrowed_books:
            return False
        else:
            self.borrowed_books[book_title] = member_id
            with open("borrowed_books.txt", "a+") as borrow_file:
                borrow_file.write(f"{member_id},{book_title}\n")
            return True

    """Method to give back a book. It takes a member ID and a book title as arguments. It checks if the book is in the
    borrowed books dictionary and if the member ID matches the one in the dictionary. If so, it removes the book from the
    borrowed books dictionary and the borrowed_books.txt file. If not, it returns False."""
    def give_back_book(self, member_id, book_title):
        if book_title in self.borrowed_books and self.borrowed_books[book_title] == member_id:
            del self.borrowed_books[book_title]
            with open("borrowed_books.txt", "r") as borrow_file:
                lines = borrow_file.readlines()
            with open("borrowed_books.txt", "w") as borrow_file:
                for line in lines:
                    if f"{member_id},{book_title}" not in line:
                        borrow_file.write(line)
            return True
        else:
            return False


class MemberManager:
    def __init__(self):
        self.file = open("members.txt", "a+")
        self.members = {}

    def __del__(self):
        self.file.close()

    def add_member(self, name, member_id):
        self.members[member_id] = name
        self.file.write(f"{name},{member_id}\n")


def main():
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
