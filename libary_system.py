from datetime import datetime

books = [
    {
        "book_id": 1,
        "title": "Python Basics",
        "author": "John",
        "total_copies": 3,
        "available_copies": 2
    },
    {
        "book_id": 2,
        "title": "Machine Learning",
        "author": "David",
        "total_copies": 6,
        "available_copies": 6
    },
    {
        "book_id": 3,
        "title": "Deep Learning",
        "author": "Andrew",
        "total_copies": 1,
        "available_copies": 1
    }
]

members = [
    {
        "member_id": 101,
        "member_name": "Rahul Roy",
        "phone_number": "9876543210"
    },
    {
        "member_id": 102,
        "member_name": "Amit Basu",
        "phone_number": "9876543211"
    }
]

borrow_records = [
    {
        "member_id": 101,
        "book_id": 1,
        "issue_date": "10-1-2026",
        "return_date": "10-6-2026"
    }
]


def add_book(id, title, author, total_copies, available_copies):

    new_dict = {}

    new_dict["book_id"] = id
    new_dict["title"] = title
    new_dict["author"] = author
    new_dict["total_copies"] = total_copies
    new_dict["available_copies"] = available_copies
    books.append(new_dict)
    print(books)


def remove_book(id):
    for book_dict in books:
        book_id = book_dict["book_id"]
        total_copies = book_dict["total_copies"]
        available_copies = book_dict["available_copies"]
        if id == book_id and total_copies == available_copies:
            books.remove(book_dict)
            print(books)
            break
    else:
        print("All copy not in libary")


def issue_book(member_id, book_id, issue_date, return_date):

    issue_dict = {}

    for book_dict in books:
        b_id = book_dict["book_id"]
        b_copy = book_dict["available_copies"]

        if b_id == book_id and b_copy > 0:
            book_dict["available_copies"] -= 1
            issue_dict["member_id"] = member_id
            issue_dict["book_id"] = book_id
            issue_dict["issue_date"] = issue_date
            issue_dict["return_date"] = return_date
            borrow_records.append(issue_dict)
            print(issue_dict)
            print(book_dict)
            break
    else:
        print("Book is not available")


def return_book(member_id, book_id, current_date):
    for borrow_dict in borrow_records:
        m_id = borrow_dict["member_id"]
        b_id = borrow_dict["book_id"]

        if m_id == member_id and b_id == book_id:
            return_date = borrow_dict["return_date"]
            fine_calculation(return_date, current_date)

            print(f"User issue book & date details : {borrow_dict}")
            borrow_records.remove(borrow_dict)

            for book_dict in books:
                b1_id = book_dict["book_id"]
                if b1_id == book_id:
                    book_dict["available_copies"] += 1
                    print(f"Book details : {book_dict}")
                    return

    else:
        print("No record found !")


def search_book(id):
    for book_dict in books:
        book_id = book_dict["book_id"]
        if book_id == id:
            print(book_dict)
            break


def fine_calculation(return_date, current_date):

    # Convert strings to datetime objects matching the format
    date1 = datetime.strptime(return_date, "%d-%m-%Y")
    date2 = datetime.strptime(current_date, "%d-%m-%Y")

    if date2 > date1:
        total_day = (date2 - date1).days
        fine = (total_day * 2)
        print(f"Fine = {fine}")

    else:
        print("No Fine..")


def find_bookID(id):
    for my_dict in books:
        book_id = my_dict["book_id"]
        if id == book_id:
            return True

    return False


def find_memberID(id):
    for member_dict in members:
        member_id = member_dict["member_id"]
        if id == member_id:
            return True

    return False


def add_member(id, name, phone_no):

    member_dict = {}

    member_dict["member_id"] = id
    member_dict["member_name"] = name
    member_dict["phone_number"] = phone_no
    members.append(member_dict)
    print(members)


while True:
    user_input = int(input(
        "\nChoose an operation:\n"
        "1. Add a book\n"
        "2. Remove a book\n"
        "3. Issue a book to a member\n"
        "4. Return a book\n"
        "5. Search for a book\n"
        "6. Add a member\n"
        "7. Exit\n"
        "Enter your choice: "
    ))

    if user_input == 1:
        book_id = int(input("Enter book ID: "))

        value = find_bookID(book_id)
        if value != True:
            book_title = input("Enter book title: ")
            book_author = input("Enter author name: ")
            total_copy = int(input("Enter total number of copies: "))
            available_copy = total_copy
            add_book(book_id, book_title, book_author,
                     total_copy, available_copy)
        else:
            print("Book ID always unique..")

    elif user_input == 2:
        book_id = int(input("Enter book ID: "))

        value = find_bookID(book_id)
        if value == True:
            remove_book(book_id)
        else:
            print("Book id does not match..")

    elif user_input == 3:
        member_id = int(input("Enter member ID : "))

        member_value = find_memberID(member_id)
        if member_value != True:
            print("Please enter correct member ID")
        else:
            book_id = int(input("Enter book ID : "))
            book_value = find_bookID(book_id)
            if book_value != True:
                print("Please enter correct book ID")
            else:
                issue_date = input("Enter book issue date (dd-mm-YYYY) : ")
                return_date = input("Enter book return date (dd-mm-YYYY) : ")
                issue_book(member_id, book_id, issue_date, return_date)

    elif user_input == 4:
        member_id = int(input("Enter member ID : "))

        member_value = find_memberID(member_id)
        if member_value != True:
            print("Member ID does not match")
        else:
            book_id = int(input("Enter book ID : "))
            book_value = find_bookID(book_id)
            if book_value != True:
                print("Book ID does not match")
            else:
                today_date = input("Enter Today's date (dd-mm-YYYY) : ")
                return_book(member_id, book_id, today_date)

    elif user_input == 5:
        book_id = int(input("Enter book ID : "))

        book_value = find_bookID(book_id)
        if book_value != True:
            print("Please Enter a correct book ID")
        else:
            search_book(book_id)

    elif user_input == 6:
        member_id = int(input("Enter member ID : "))

        member_value = find_memberID(member_id)
        if member_value == True:
            print("Member ID always unique")
        else:
            member_name = input("Enter member name : ")
            member_phone_no = int(input("Enter member phone no. : "))
            add_member(member_id, member_name, member_phone_no)

    elif user_input == 7:
        break

    else:
        print("Enter a correct number")
