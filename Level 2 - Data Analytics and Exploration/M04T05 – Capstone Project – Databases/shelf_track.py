"""
Created on Fri Sep 12 12:39:50 2025
@author: juleigar

Ebookstore Manager
This program allows users to manage books and authors.
Users can add, update, search, delete books, and view all book details.
"""

import sqlite3
import sys
from tabulate import tabulate

# ------------------------ DATABASE HANDLER ------------------------
class Database:
    def __init__(self, db_name="ebookstore.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            sys.exit()

    def close(self):
        if self.conn:
            self.conn.close()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def execute(self, query, params=()):
        try:
            self.cursor.execute(query, params)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()


# ------------------------ BOOK & AUTHOR MANAGEMENT ------------------------
class BookManager:
    def __init__(self, db: Database):
        self.db = db
        self.create_tables()

    # --- TABLES ---
    def create_tables(self):
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS author(
                id INTEGER PRIMARY KEY,
                name TEXT,
                country TEXT
            )
        """)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY,
                title TEXT,
                authorid INTEGER,
                qty INTEGER,
                FOREIGN KEY(authorid) REFERENCES author(id)
            )
        """)
        self.db.commit()

    # --- ADD NEW BOOK ---
    def add_book(self):
        book_id = self.get_valid_id("Enter book id (4 digits): ")
        title = input("Enter Book Title: ").strip()
        author_id = self.get_valid_id("Enter author id (4 digits): ")
    
        # Check if author exists
        self.db.execute("SELECT * FROM author WHERE id = ?", (author_id,))
        author = self.db.fetchone()
        if not author:
            print("Author not found. Please enter author details.")
            author_name = input("Enter author name: ").strip()
            author_country = input("Enter author country: ").strip()
            self.db.execute(
                "INSERT INTO author(id, name, country) VALUES (?, ?, ?)",
                (author_id, author_name, author_country)
            )
            self.db.commit()
            print("Author added successfully.")
    
        qty = self.get_valid_int("Enter number of books: ")
        self.db.execute(
            "INSERT INTO book(id, title, authorid, qty) VALUES (?, ?, ?, ?)",
            (book_id, title, author_id, qty)
        )
        self.db.commit()
        print("Book added successfully.")


    # --- UPDATE BOOK ---
    def update_book(self):
        book_id = self.get_valid_id("Enter the ID of the book to update: ")
    
        # Show current book and author info
        self.db.execute("""
            SELECT b.title, b.qty, a.id, a.name, a.country
            FROM book b
            INNER JOIN author a ON b.authorid = a.id
            WHERE b.id = ?
        """, (book_id,))
        result = self.db.fetchone()
    
        if not result:
            print("Book not found.")
            return
    
        title, qty, author_id, author_name, author_country = result
        print(f"Current Book Info:\nTitle: {title}\nQty: {qty}\nAuthor: {author_name}\nCountry: {author_country}")
    
        # Update book details
        new_title = input("Enter new title (or press Enter to keep current): ").strip()
        if new_title:
            self.db.execute("UPDATE book SET title = ? WHERE id = ?", (new_title, book_id))
    
        new_qty = input("Enter new quantity (or press Enter to keep current): ").strip()
        if new_qty:
            new_qty = int(new_qty)
            self.db.execute("UPDATE book SET qty = ? WHERE id = ?", (new_qty, book_id))
    
        # Update author details
        update_author = input("Do you want to update the author info? (yes/no): ").lower()
        if update_author == "yes":
            new_author_name = input(f"Enter new author name (or press Enter to keep {author_name}): ").strip()
            new_author_country = input(f"Enter new author country (or press Enter to keep {author_country}): ").strip()
            if new_author_name:
                self.db.execute("UPDATE author SET name = ? WHERE id = ?", (new_author_name, author_id))
            if new_author_country:
                self.db.execute("UPDATE author SET country = ? WHERE id = ?", (new_author_country, author_id))
    
        self.db.commit()
        print("Book and author updated successfully.")


    # --- SEARCH BOOK ---
    def search_book(self):
        print("Search by:\n1 - ID\n2 - Title\n3 - AuthorID")
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            book_id = self.get_valid_id("Enter book id: ")
            self.db.execute("SELECT * FROM book WHERE id = ?", (book_id,))
        elif choice == "2":
            title = input("Enter book title: ").strip().lower()
            self.db.execute("SELECT * FROM book WHERE LOWER(title) LIKE ?", ('%'+title+'%',))
        elif choice == "3":
            author_id = self.get_valid_id("Enter author id: ")
            self.db.execute("SELECT * FROM book WHERE authorid = ?", (author_id,))
        else:
            print("Invalid choice.")
            return

        books = self.db.fetchall()
        headers = ("ID", "Title", "AuthorID", "Qty")
        if books:
            print("\nSearch Results:")
            print(tabulate(books, headers=headers, tablefmt="grid"))
        else:
            print("No books found.")

    # --- VIEW ALL BOOKS IN USER-FRIENDLY FORMAT ---
    def view_all_books(self):
        self.db.execute("""
            SELECT b.title, a.name, a.country
            FROM book b
            INNER JOIN author a ON a.id = b.authorid
        """)
        books = self.db.fetchall()

        if books:
            print("\nDetails\n" + "-"*50)
            for title, author_name, country in books:
                print(f"Title: {title}")
                print(f"Author's Name: {author_name}")
                print(f"Author's Country: {country}")
                print("-"*50)
        else:
            print("No books to view.")
            
            
            # --- DELETE BOOK ---
    def delete_book(self):
        book_id = self.get_valid_id("Enter the ID of the book to delete: ")
        # Check if book exists
        self.db.execute("SELECT title FROM book WHERE id = ?", (book_id,))
        book = self.db.fetchone()
        if not book:
            print("Book not found.")
            return
        
        confirm = input(f"Are you sure you want to delete '{book[0]}'? (yes/no): ").lower()
        if confirm == "yes":
            self.db.execute("DELETE FROM book WHERE id = ?", (book_id,))
            self.db.commit()
            print("Book deleted successfully.")
        else:
            print("Deletion cancelled.")


    # --- UTILITY FUNCTIONS ---
    def get_valid_id(self, prompt):
        while True:
            value = input(prompt).strip()
            if value.isdigit() and len(value) == 4:
                return int(value)
            print("Invalid input. Must be a 4-digit number.")

    def get_valid_int(self, prompt):
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                return int(value)
            print("Invalid input. Must be an integer.")


# ------------------------ MAIN PROGRAM ------------------------
def main():
    db = Database()
    manager = BookManager(db)

    # Prepopulate authors if empty
    db.execute("SELECT COUNT(*) FROM author")
    if db.fetchone()[0] == 0:
        initial_authors = [
            (1290, "Charles Dickens", "England"),
            (8937, "J.K. Rowling", "England"),
            (2356, "C.S. Lewis", "Ireland"),
            (6380, "J.R.R. Tolkien", "South Africa"), 
            (5620, "Lewis Carroll", "England")
        ]
        db.cursor.executemany("INSERT INTO author(id, name, country) VALUES (?, ?, ?)", initial_authors)
        db.commit()

    # Prepopulate books if empty
    db.execute("SELECT COUNT(*) FROM book")
    if db.fetchone()[0] == 0:
        initial_books = [
            (3001, "A Tale of Two Cities", 1290, 30),
            (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
            (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
            (3004, "The Lord of the Rings", 6380, 37),
            (3005, "Alice’s Adventures in Wonderland", 5620, 12),
        ]
        db.cursor.executemany("INSERT INTO book(id, title, authorid, qty) VALUES (?, ?, ?, ?)", initial_books)
        db.commit()

    # Menu loop
    while True:
        menu = input(
            "\nSelect one of the following options:\n"
            "a  - add book\n"
            "up - update book\n"
            "del - delete book\n"
            "s  - search book\n"
            "v  - view details of all books\n"
            "e  - exit\n: "
        ).lower()

        if menu == "a":
            manager.add_book()
        elif menu == "up":
            manager.update_book()
        elif menu == "del":
            manager.delete_book()
        elif menu == "s":
            manager.search_book()
        elif menu == "v":
            manager.view_all_books()
        elif menu == "e":
            db.close()
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
