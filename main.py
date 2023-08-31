import sqlite3
import bcrypt, time
from colorama import Fore

connection_book = sqlite3.connect("Book.db")
con1 = sqlite3.connect("Users.db")
con2 = sqlite3.connect("Library.db")

cursor_book = connection_book.cursor()
cursor_user = con1.cursor()
cursor2 = con2.cursor()
# cursor_user.execute("DROP TABLE IF EXISTS Users")
cursor2.execute("DROP TABLE IF EXISTS Library")
query_one = """CREATE TABLE Users(
        username CHAR(20) NOT NULL, 
        password1 CHAR(20) NOT NULL, 
        password2 CHAR(20) NOT NULL, 
        is_staff INT, 
        is_login INT 
        );"""
query_two = """CREATE TABLE Library(
        NAME CHAR(20) NOT NULL
        );"""

# -------------------------------Creating and filling the book db--------------
cursor_book.execute("DROP TABLE IF EXISTS Book")
create_table_book_query = '''
CREATE TABLE IF NOT EXISTS Book (
    ID INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Category TEXT NOT NULL,
    Author TEXT NOT NULL,
    Pages INTEGER NOT NULL,
    Available INTEGER 
);
'''
insert_query = '''
INSERT INTO Book (ID, Title, Category, Author, Pages, Available)
VALUES (?, ?, ?, ?, ?, ?);
'''
book_list = [
    (1, "To Kill a Mockingbird", "Fiction", "Harper Lee", 336, 1),
    (2, "1984", "Fiction", "George Orwell", 328, 1),
    (3, "Pride and Prejudice", "Fiction", "Jane Austen", 432, 1),
    (4, "The Great Gatsby", "Fiction", "F. Scott Fitzgerald", 180, 1),
    (5, "Harry Potter and the Sorcerer's Stone", "Fantasy", "J.K. Rowling", 320, 1),
    (6, "The Lord of the Rings", "Fantasy", "J.R.R. Tolkien", 1178, 1),
    (7, "The Catcher in the Rye", "Fiction", "J.D. Salinger", 277, 1),
    (8, "Animal Farm", "Fiction", "George Orwell", 112, 1),
    (9, "Brave New World", "Fiction", "Aldous Huxley", 288, 1),
    (10, "The Hobbit", "Fantasy", "J.R.R. Tolkien", 310, 1),
    (11, "The Da Vinci Code", "Mystery", "Dan Brown", 592, 1),
    (12, "The Hunger Games", "Young Adult", "Suzanne Collins", 374, 1),
    (13, "The Alchemist", "Fiction", "Paulo Coelho", 208, 1),
    (14, "Fahrenheit 451", "Science Fiction", "Ray Bradbury", 249, 1),
    (15, "Gone with the Wind", "Fiction", "Margaret Mitchell", 960, 1),
    (16, "Jane Eyre", "Fiction", "Charlotte Bronte", 532, 1),
    (17, "The Odyssey", "Mythology", "Homer", 541, 1),
    (18, "The Divine Comedy", "Poetry", "Dante Alighieri", 928, 1),
    (19, "Moby-Dick", "Fiction", "Herman Melville", 720, 1),
    (20, "The Adventures of Huckleberry Finn", "Fiction", "Mark Twain", 366, 1),
    (21, "Harry Potter and the Chamber of Secrets", "Fantasy", "J.K. Rowling", 352, 1),
    (22, "Harry Potter and the Prisoner of Azkaban", "Fantasy", "J.K. Rowling", 464, 1),
    (23, "Harry Potter and the Goblet of Fire", "Fantasy", "J.K. Rowling", 734, 1),
    (24, "Harry Potter and the Order of the Phoenix", "Fantasy", "J.K. Rowling", 870, 1),
    (25, "Harry Potter and the Half-Blood Prince", "Fantasy", "J.K. Rowling", 652, 1),
    (26, "Harry Potter and the Deathly Hallows", "Fantasy", "J.K. Rowling", 759, 1),
    (27, "Cosmos", "Science", "Carl Sagan", 432, 1),
    (28, "The Geography of Bliss", "Geography", "Eric Weiner", 353, 1),
    (29, "The Code Book", "Maths", "Simon Singh", 432, 1),
    (30, "The Feynman Lectures on Physics", "Physics", "Richard P. Feynman", 1554, 1),
    (
        31, "The Elements: A Visual Exploration of Every Known Atom in the Universe", "Chemistry", "Theodore Gray", 240,
        1),
    (32, "Automate the Boring Stuff with Python", "Programming", "Al Sweigart", 504, 1),
    (33, "Cracking the Coding Interview", "Programming", "Gayle Laakmann McDowell", 687, 1),
    (34, "The Complete Guide to Fasting", "Health", "Jason Fung", 304, 1),
    (35, "The Omnivore's Dilemma", "Food", "Michael Pollan", 450, 1),
    (36, "Thinking, Fast and Slow", "Psychology", "Daniel Kahneman", 499, 1),
    (37, "SPQR: A History of Ancient Rome", "Roman", "Mary Beard", 608, 1),
    (38, "The Film Experience: An Introduction", "Cinema", "Timothy Corrigan", 464, 1),
    (39, "Sapiens: A Brief History of Humankind", "History", "Yuval Noah Harari", 443, 1),
    (40, "The Innovators: How a Group of Hackers, Geniuses, and Geeks Created the Digital Revolution", "History",
     "Walter Isaacson", 560, 1),
    (41, "Longitude: The True Story of a Lone Genius Who Solved the Greatest Scientific Problem of His Time", "History",
     "Dava Sobel", 184, 1),
    (42, "The Immortal Life of Henrietta Lacks", "History", "Rebecca Skloot", 381, 1),
    (43, "The Sixth Extinction: An Unnatural History", "History", "Elizabeth Kolbert", 336, 1),
    (44, "How the Mind Works", "Psychology", "Steven Pinker", 672, 1),
    (45, "Into the Wild", "Geography", "Jon Krakauer", 207, 1),
    (46, "The Pragmatic Programmer: Your Journey To Mastery", "Programming", "Andrew Hunt, David Thomas", 352, 1),
    (47, "The Body: A Guide for Occupants", "Health", "Bill Bryson", 464, 1),
    (48, "Slaughterhouse-Five", "Science", "Kurt Vonnegut", 275, 1),
    (49, "The Gene: An Intimate History", "Science", "Siddhartha Mukherjee", 608, 1),
    (
        50, "The Innovators Dilemma: When New Technologies Cause Great Firms to Fail", "Business",
        "Clayton M. Christensen",
        286, 1),
    (51, "The Codebreakers: The Comprehensive History of Secret Communication from Ancient Times to the Internet",
     "History", "David Kahn", 1184, 1),
    (52, "A Short History of Nearly Everything", "Science", "Bill Bryson", 544, 1),
    (53, "The Wright Brothers", "History", "David McCullough", 336, 1),
    (54, "The Power of Habit: Why We Do What We Do in Life and Business", "Psychology", "Charles Duhigg", 400, 1),
    (55, "The Road to Serfdom", "Philosophy", "F.A. Hayek", 274, 1),
    (56, "The Origins of Totalitarianism", "History", "Hannah Arendt", 576, 1),
    (57, "The Brothers Karamazov", "Philosophy", "Fyodor Dostoevsky", 796, 1),
    (58, "The God Delusion", "Philosophy", "Richard Dawkins", 464, 1),
    (59, "Siddhartha", "Philosophy", "Hermann Hesse", 152, 1),
    (60, "The Art of Happiness", "Psychology", "Dalai Lama", 320, 1),
    (61, "The Interpretation of Dreams", "Psychology", "Sigmund Freud", 496, 1),
    (62, "The Road Less Traveled: A New Psychology of Love, Traditional Values and Spiritual Growth", "Psychology",
     "M. Scott Peck", 315, 1),
    (63, "The Godfather", "Roman", "Mario Puzo", 448, 1),
    (64, "The Hunchback of Notre-Dame", "Roman", "Victor Hugo", 624, 1),
    (65, "The Princess Bride", "Roman", "William Goldman", 399, 1),
    (66, "1984", "Roman", "George Orwell", 328, 1),
    (67, "Brave New World", "Roman", "Aldous Huxley", 288, 1),
    (68, "Jurassic Park", "Science", "Michael Crichton", 448, 1),
    (69, "The Intelligent Investor", "Business", "Benjamin Graham", 640, 1),
    (70, "The Selfish Gene", "Science", "Richard Dawkins", 360, 1),
    (71, "The Elements of Style", "Language", "William Strunk Jr.", 105, 1),
    (72, "The Art of War", "Philosophy", "Sun Tzu", 273, 1),
    (73, "Guns, Germs, and Steel: The Fates of Human Societies", "History", "Jared Diamond", 496, 1),
    (74, "Sapiens: A Brief History of Humankind", "History", "Yuval Noah Harari", 443, 1),
    (75, "The Emperor of All Maladies: A Biography of Cancer", "Science", "Siddhartha Mukherjee", 608, 1),
    (76, "Freakonomics: A Rogue Economist Explores the Hidden Side of Everything", "Economics",
     "Steven D. Levitt, Stephen J. Dubner", 336, 1),
    (77, "The Interpretation of Dreams", "Psychology", "Sigmund Freud", 496, 1),
    (78, "The Catcher in the Rye", "Roman", "J.D. Salinger", 277, 1),
    (79, "A People's History of the United States", "History", "Howard Zinn", 729, 1),
    (80, "Godel, Escher, Bach: An Eternal Golden Braid", "Science", "Douglas R. Hofstadter", 822, 1),
    (81, "The Name of the Rose", "Roman", "Umberto Eco", 536, 1),
    (82, "The Outsiders", "Roman", "S.E. Hinton", 192, 1),
    (83, "The Fountainhead", "Philosophy", "Ayn Rand", 752, 1),
    (84, "A Brief History of Time", "Science", "Stephen Hawking", 212, 1),
    (85, "The Great Gatsby", "Roman", "F. Scott Fitzgerald", 180, 1),
    (86, "The Hitchhiker's Guide to the Galaxy", "Science", "Douglas Adams", 224, 1),
    (87, "The Art of Happiness", "Psychology", "Dalai Lama", 320, 1),
    (88, "Fahrenheit 451", "Science", "Ray Bradbury", 249, 1),
    (89, "The Book Thief", "Roman", "Markus Zusak", 552, 1),
    (90, "The Color Purple", "Roman", "Alice Walker", 304, 1),
    (91, "The Picture of Dorian Gray", "Roman", "Oscar Wilde", 254, 1),
    (92, "The Scarlet Letter", "Roman", "Nathaniel Hawthorne", 232, 1),
    (93, "War and Peace", "History", "Leo Tolstoy", 1296, 1),
    (94, "The Hobbit", "Fantasy", "J.R.R. Tolkien", 310, 1),
    (95, "Pride and Prejudice", "Roman", "Jane Austen", 432, 1),
    (96, "Moby-Dick", "Roman", "Herman Melville", 720, 1),
    (97, "Crime and Punishment", "Roman", "Fyodor Dostoevsky", 430, 1),
    (98, "Lord of the Flies", "Roman", "William Golding", 182, 1),
    (99, "The Old Man and the Sea", "Roman", "Ernest Hemingway", 128, 1),
    (100, "Don Quixote", "Roman", "Miguel de Cervantes", 1023, 1),
    (101, "The Odyssey", "Roman", "Homer", 541, 1),
    (102, "The Divine Comedy", "Poetry", "Dante Alighieri", 928, 1),
    (103, "One Hundred Years of Solitude", "Roman", "Gabriel García Márquez", 417, 1),
    (104, "Anna Karenina", "Roman", "Leo Tolstoy", 864, 1),
    (105, "Frankenstein", "Roman", "Mary Shelley", 280, 1),
    (106, "Great Expectations", "Roman", "Charles Dickens", 505, 1),
    (107, "Heart of Darkness", "Roman", "Joseph Conrad", 78, 1),
    (108, "Dracula", "Roman", "Bram Stoker", 418, 1),
    (109, "1984", "Roman", "George Orwell", 328, 1),
    (110, "To Kill a Mockingbird", "Roman", "Harper Lee", 336, 1),
    (111, "The Grapes of Wrath", "Roman", "John Steinbeck", 464, 1),
    (112, "Jane Eyre", "Roman", "Charlotte Bronte", 532, 1),
    (113, "Wuthering Heights", "Roman", "Emily Bronte", 348, 1),
    (114, "The Catcher in the Rye", "Roman", "J.D. Salinger", 277, 1),
    (115, "The Hobbit", "Fantasy", "J.R.R. Tolkien", 310, 1),
    (116, "The Great Gatsby", "Roman", "F. Scott Fitzgerald", 180, 1),
    (117, "Animal Farm", "Roman", "George Orwell", 112, 1),
    (118, "The Lord of the Rings", "Fantasy", "J.R.R. Tolkien", 1178, 1),
    (119, "The Chronicles of Narnia", "Fantasy", "C.S. Lewis", 767, 1),
    (120, "The Da Vinci Code", "Mystery", "Dan Brown", 592, 1),
    (121, "Harry Potter and the Sorcerer's Stone", "Fantasy", "J.K. Rowling", 320, 1),
    (122, "Harry Potter and the Chamber of Secrets", "Fantasy", "J.K. Rowling", 352, 1),
    (123, "Harry Potter and the Prisoner of Azkaban", "Fantasy", "J.K. Rowling", 464, 1),
    (124, "Harry Potter and the Goblet of Fire", "Fantasy", "J.K. Rowling", 734, 1),
    (125, "Harry Potter and the Order of the Phoenix", "Fantasy", "J.K. Rowling", 870, 1),
    (126, "Harry Potter and the Half-Blood Prince", "Fantasy", "J.K. Rowling", 652, 1),
    (127, "Harry Potter and the Deathly Hallows", "Fantasy", "J.K. Rowling", 759, 1),
    (128, "The Hunger Games", "Young Adult", "Suzanne Collins", 374, 1),
    (129, "The Alchemist", "Fiction", "Paulo Coelho", 208, 1),
    (130, "Fahrenheit 451", "Science", "Ray Bradbury", 249, 1),
    (131, "Gone with the Wind", "Roman", "Margaret Mitchell", 960, 1),
    (132, "The Girl with the Dragon Tattoo", "Mystery", "Stieg Larsson", 672, 1),
    (133, "Divergent", "Young Adult", "Veronica Roth", 496, 1),
    (134, "The Help", "Fiction", "Kathryn Stockett", 451, 1),
    (135, "The Book Thief", "Roman", "Markus Zusak", 552, 1),
    (136, "The Maze Runner", "Young Adult", "James Dashner", 375, 1),
    (137, "Ender's Game", "Science", "Orson Scott Card", 352, 1),
    (138, "The Fault in Our Stars", "Young Adult", "John Green", 318, 1),
    (139, "The Night Circus", "Fantasy", "Erin Morgenstern", 401, 1),
    (140, "The Stand", "Fantasy", "Stephen King", 1153, 1),
]
cursor_book.execute(create_table_book_query)
try:
    cursor_book.executemany(insert_query, book_list)
    connection_book.commit()
    print("Data insertion successful.")
except Exception as e:
    print(Fore.RED, f"Error occurred: {e}")
    connection_book.rollback()
# -------------------------------End for the book db--------------

# cursor_user.execute(query_one)
cursor2.execute(query_two)

# Variable declaration
is_staff = 1

class Book:
    def __init__(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages

class User:
    def __init__(self,username,author,pages):
        self.username=username
        self.author=author
        self.pages=pages

def sing_up(username, password, is_staff, is_login):
    if username != '' and password != '':
        cursor_user.execute('SELECT username FROM Users WHERE username=?', [username])
        if cursor_user.fetchone() is not None:
            print(Fore.RED, "ERROR: Username already exist!")
            main_window()
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

            cursor_user.execute('INSERT INTO Users VALUES (?,?,?,?,?)',
                                [username, hashed_password, hashed_password, is_staff, is_login])
            con1.commit()
            time.sleep(2)
            print(Fore.YELLOW, "Your account has been successfuly created!")
            main_window()
    else:
        print(Fore.RED, "ERROR please fill all the fields")
        main_window()


def sign_in(username, password):
    if username != '' and password != '':
        cursor_user.execute('SELECT password1,is_staff FROM Users WHERE username=?', [username])
        result = cursor_user.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                print("Loading...")
                global is_staff
                is_staff = result[1]
                time.sleep(1.5)
                print("Logged successfully!")
                main_page()
            else:
                print("Please check your password")
                main_window()
        else:
            print("Invalid username!")
            main_window()
    else:
        print("Please enter all data.")
        main_window()


def main_window():
    time.sleep(1)
    print("-*-" * 17)
    time.sleep(1)
    print("|✨📜Welcome to your library management system :📚✨ |")
    time.sleep(1)
    print("-*-" * 17)
    print("1-Register\n")
    print("2-Login\n")
    print(Fore.BLUE, "How can we help you ?\n")
    choice = input()

    if choice == "1":
        print("-*-" * 17)
        time.sleep(0.5)
        print("|✨📜Welcome to the registration page :📚✨ |")
        time.sleep(0.5)
        print("-*-" * 17)
        global is_staff
        is_staff = int(input("Please are you a staff or not : (just enter 0 for NO or 1 for YES)\n"))
        if is_staff:
            pass_ = input("Provide the pass key or exit with (4) :) : ")
            match pass_ :
                case "4":
                    main_window()
                case "/**/":
                    print("Access granted!")
                case _:
                    print("D you want to die?")
                    main_window()

        username = input("Please enter your username\n")
        password1 = input("Please enter a password\n")
        password2 = input("Please confirm your password\n")
        is_login = 1
        print(password1)
        print(password2)
        if password1 != password2:
            print("Please enter the same password for both fields!")
            print("-*-" * 17)
            time.sleep(0.4)
            main_window()
        else:
            sing_up(username, password1,
                    is_staff, is_login)
            print(Fore.GREEN, "New user created successfully")
            main_window()
    elif choice == "2":
        print("✨📜Welcome to the login page :📚✨ ")
        username = input("Please enter your username : \n")
        password = input("Please enter your password : \n")
        sign_in(username, password)
    else:
        main_window()


def print_menu():
    print(Fore.BLUE, "What do you want to do ?")
    if is_staff:
        choice_menu = input("""
                  1-See all the available books
                  2-See a particular book
                  3-Borrow a book
                  4-Exit  
                  5-Add a book    
            (Enter a number to select an option :) )
            """)
    else:
        choice_menu = input("""
                          1-See all the available books
                          2-See a particular book
                          3-Borrow a book
                          4-Exit      
                    (Enter a number to select an option :) )
                    """)

    return choice_menu


def main_page():
    choice = print_menu()
    match_choice(choice)


def match_choice(another_choice):
    match another_choice:
        case "1":
            cursor_book.execute('SELECT * FROM Book ')
            all_books = cursor_book.fetchall()
            for book in all_books:
                print(f"|  {book[0]}  {book[1]}, [{book[2]}]-->By  {book[3]}. ({book[4]} pages)|")
            another_choice = print_menu()
            match_choice(another_choice)
        case "2":
            id = input("Please can you provide me with the id of the book you want to consult ?\n")
            book = cursor_book.execute('SELECT * FROM Book WHERE ID=?', [id]).fetchone()
            print(f"|  {book[0]}  {book[1]}, [{book[2]}]-->By  {book[3]}. ({book[4]} pages)|")
            another_choice = print_menu()
            match_choice(another_choice)
        case "3":
            id = input("Please can you provide me with the id of the book you want to borrow ?\n")
            book = cursor_book.execute('SELECT * FROM Book WHERE  ID=?', [id]).fetchone()
            return_date = input("Please when are you going to come back with the borrowed book ?\n")
            if int(return_date) <= 20:
                borrow_book(book[1], id, return_date)
                another_choice = print_menu()
            else:
                print(Fore.RED, "You can just borrow a book for a maximum of 20 days!")
            match_choice(another_choice)
        case "4":
            main_window()
        case "5":
            if is_staff:
                add_book_to_database()
            else:
                print(Fore.RED, "You are trying to add a book, but you are not a staff.")
                main_page()
        case _:
            print("Please enter a valid selection (Use the different numbers...)")
            another_choice = print_menu()
            match_choice(another_choice)


def add_book_to_database():
    conn = sqlite3.connect('Book.db')
    cursor = conn.cursor()
    ID = int(input("Please enter the id of the book"))
    Title = input("Please enter the title of the book")
    Category = input("Pleas enter the category of the book")
    Author = input("Please enter the name of the author of the book")
    Pages = input("Please enter the numner of pages of the book")
    Available = 1
    insert_query_book = '''
    INSERT INTO book (ID, Title, Category, Author, Pages, Available)
    VALUES (?, ?, ?, ?, ?, ?)
    '''

    try:
        cursor.execute(insert_query_book, (ID, Title, Category, Author, Pages, Available))
        conn.commit()
        print(Fore.BLUE, "New book added successfully.")
    except Exception as e:
        print(Fore.RED, f"Error occurred while adding the book: {e}")
        conn.rollback()
    main_page()


def borrow_book(title, book_id, return_date):
    cursor_book.execute(f''' SELECT * FROM Book WHERE ID={book_id} ''')
    print(Fore.BLUE,
          f"Thanks for your interest in the \"{title}\" book, Good reading.\n")
    update_query = '''
        UPDATE Book
        SET Available = ?
        WHERE ID = ?
        '''
    try:
        print(Fore.YELLOW, f"The book {title} is now unavailable until {return_date} days.")
        cursor_book.execute(update_query, (0, book_id))
        connection_book.commit()
    except Exception as e_borrow:
        print(Fore.RED, f"Error occurred while updating: {e_borrow}")
        connection_book.rollback()
        cursor_book.close()
        connection_book.close()


main_window()
