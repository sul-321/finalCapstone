import sqlite3

def main():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INT PRIMARY KEY NOT NULL, 
            Title TEXT NOT NULL, 
            Author TEXT NOT NULL, 
            Qty INT NOT NULL 
        )
    ''')

    books = [
        (1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 10),
        (2, "To Kill a Mockingbird", "Harper Lee", 20),
        (3, "The Lord of the Rings", "J.R.R. Tolkien", 15),
        (4, "Pride and Prejudice", "Jane Austen", 5),
        (5, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 25)
    ]
    c.executemany("INSERT INTO books (id, Title, Author, Qty) VALUES (?, ?, ?, ?)", books)

    while True:
        print("\nBookstore Clerk Menu")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            id = int(input("Enter book id: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            qty = int(input("Enter book quantity: "))
            c.execute("INSERT INTO books (id, Title, Author, Qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))

        elif choice == 2:
            id = int(input("Enter book id to update: "))
            title = input("Enter updated book title: ")
            author = input("Enter updated book author: ")
            qty = int(input("Enter updated book quantity: "))
            c.execute("UPDATE books SET Title=?, Author=?, Qty=? WHERE id=?", (title, author, qty, id))

        elif choice == 3:
            id = int(input("Enter book id to delete: "))
            c.execute("DELETE FROM books WHERE id=?", (id,))

        elif choice == 4:
            search_term = input("Enter search term: ")
            c.execute("SELECT * FROM books WHERE Title LIKE ? OR Author LIKE ?", (f"%{search_term}%", f"%{search_term}%"))
            books = c.fetchall()
            print("\nSearch Results:")
            for book in books:
                print(f"{book[0]}: {book[1]} by {book[2]} ({book[3]} copies)")

        elif choice == 0:
            conn.commit()
            conn.close()
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
