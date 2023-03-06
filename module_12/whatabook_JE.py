import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
def show_menu():
    print("\n  -- Main Menu --")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      <Example enter: 1 for book listing>: '))

        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_books(_cursor):
    # inner join query 
    query = "SELECT book_id, book_name, author, details FROM book"

    # execute the query
    cursor.execute(query)

    # fetch all the results from the cursor object 
    books = cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    # iterate over the book data set and display the results 
    for book in books:
        book_id, book_name, author, details = book
        print(f"  Book Name: {book_name}\n  Author: {author}\n  Details: {details}\n")


def show_locations(_cursor):
    _cursor.execute("SELECT store_id, location from store")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_user():
    """ Validates the user's ID. """
    while True:
        try:
            user_id = int(input('\n Enter a customer id <Example 1 for user_id 1>: '))
            
            if user_id < 0 or user_id > 3:
                print("\n Invalid customer number, please enter a number between 0 and 3.")
            else:
                return user_id
        except ValueError:
            print("\n Invalid input, please enter a number between 0 and 3.")

def show_account_menu():
#Show account menu - used notes for formatting
    try:
        print("\n-- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('Ex: Enter 1 for wishlist'))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    print("\n        -- DISPLAYING WISHLIST ITEMS --")
    #execute the inner join commands to show wishlist correctly
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    #fetch all books in wishlist
    wishlist = _cursor.fetchall()

    #Print out books in wishlist
    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
#Look for books not in user list
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_added = _cursor.fetchall()
    print("\n        -- DISPLAYING AVAILABLE BOOKS --")
    for book in books_added:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    #error handling
    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor() # cursor for MySQL queries

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = show_menu() # show the main menu 

    while user_selection != 4:

        #if the user picks one, show books
        if user_selection == 1:
            show_books(cursor)

        #if the user picks option two, show store locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user picks option three, validate their user with the user ID picked
        # call the show_account_menu() to keep option three picked
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                #Show Wishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call books to add to show books
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the book list
                    show_books_to_add(cursor, my_user_id)

                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add book to wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if account_option is not between 0 and 3, retry
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")


                account_option = show_account_menu()
        
        # if user is not 0-4, display invalid user error
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # show the main menu if else fails
        user_selection = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()