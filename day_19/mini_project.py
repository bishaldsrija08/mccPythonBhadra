# 1. Create an empty dictionary to store book-author pairs
favorite_books = {}

# 2. Start an infinite loop to show the menu

while True:
    print("\nFavorite Books Manager")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Author")
    print("4. Delete Book")
    print("5. Exit")

    choice = int(input("Choose an option (1-5): "))

    if choice == 1:
        book = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        favorite_books[book] = author
        print(f"Added '{book}' by {author}.")
    elif choice == 2:
        if not favorite_books:
            print("No books in the list.")
        else:
            print("Favorite Books:")
            for book, author in favorite_books.items():
                print(f"'{book}' by {author}")
    elif choice == 3:
        book = input("Enter the book title to update: ")
        if book in favorite_books:
            new_author = input("Enter the new author's name:")
            favorite_books[book] = new_author
            print(f"Updated '{book}' to be by {new_author}.")
        else:
            print(f"'{book}' not found in the list.")
    elif choice == 4:
        book = input("Enter the book title to delete: ")
        if book in favorite_books:
            del favorite_books[book]
            print(f"Deleted '{book}' from the list.")
        else:
            print(f"'{book}' not found in the list.")
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break