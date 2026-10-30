bank_acoount = [
    {"name": "Suman", "account_no": 12345,
        "balance": 10_000, "mobile_no": 9876543210},
    {"name": "Rahul", "account_no": 54321,
        "balance": 20_000, "mobile_no": 9876598765},
    {"name": "Saikat", "account_no": 98765,
        "balance": 30_000, "mobile_no": 9876512345}
]


def create_account(user_name, user_account_no, user_balance, user_mobile_no):
    new_account = {}
    new_account["name"] = user_name
    new_account["account_no"] = user_account_no
    new_account["balance"] = user_balance
    new_account["mobile_no"] = user_mobile_no
    bank_acoount.append(new_account)
    print(bank_acoount)


def deposit_money(user_account_no, money):
    for my_dict in bank_acoount:
        account_no = my_dict["account_no"]
        if user_account_no == account_no:
            my_dict["balance"] += money
            print(
                f"Total balance : {my_dict["balance"]}\nUser details : {my_dict}")


def withdraw_money(user_account_no, money):
    for my_dict in bank_acoount:
        account_no = my_dict["account_no"]
        if user_account_no == account_no:
            if my_dict["balance"] >= money:
                my_dict["balance"] -= money
                print(
                    f"Total balance : {my_dict["balance"]}\nUser details : {my_dict}")
                return
            else:
                print("Insufficient balance in your account")


def check_balance(user_account_no):
    for my_dict in bank_acoount:
        account_no = my_dict["account_no"]
        if user_account_no == account_no:
            print(f"Total balance : {my_dict["balance"]}")


def transfer_money(user_account_no, other_account_no, amount):

    for my_dict in bank_acoount:
        account_no = my_dict["account_no"]
        for other_dict in bank_acoount:
            other_account = other_dict["account_no"]
            if user_account_no == account_no and other_account_no == other_account:
                if my_dict["balance"] >= amount:
                    my_dict["balance"] -= amount
                    other_dict["balance"] += amount
                    print(my_dict)
                    print(other_dict)
                    break
                else:
                    print("Insufficient balance")


def exist_account(user_account_no):

    for my_dict in bank_acoount:
        account_no = my_dict["account_no"]
        if user_account_no == account_no:
            return True

    return False


while True:
    operation = int(input(
        "Select an operation:\n"
        "Press 1: Create an account\n"
        "Press 2: Deposit money\n"
        "Press 3: Withdraw money\n"
        "Press 4: Check account balance\n"
        "Press 5: Transfer money\n"
        "Press 6: Exit\n"
        "Enter your choice: "
    ))

    if operation == 1:
        account_no = int(input("Enter user account number : "))
        user = exist_account(account_no)

        if user != True:
            name = input("Enter user name : ")
            balance = int(input("Enter user amount : "))
            mobile_no = int(input("Enter user mobile number : "))
            if balance > 0:
                create_account(name, account_no, balance, mobile_no)
            else:
                print("Amount should be positive")
        else:
            print("Account number already exist.\nAcoount number always unique...")

    elif operation == 2:
        account_no = int(input("Enter user account number : "))
        user = exist_account(account_no)
        if user == True:
            balance = int(input("Enter Deposit amount : "))
            if balance > 0:
                deposit_money(account_no, balance)
            else:
                print("amount should be positive..")
        else:
            print("Account number does not exist..")

    elif operation == 3:
        account_no = int(input("Enter user account number : "))
        user = exist_account(account_no)
        if user == True:
            balance = int(input("Enter Withdraw amount : "))
            if balance > 0:
                withdraw_money(account_no, balance)
            else:
                print("amount should be positive..")
        else:
            print("Account number does not exist..")

    elif operation == 4:
        account_no = int(input("Enter user account number : "))
        user = exist_account(account_no)
        if user == True:
            check_balance(account_no)
        else:
            print("Account number does not exist..")

    elif operation == 5:
        user_account_no = int(input("Enter user account number : "))
        user = exist_account(user_account_no)
        other_account_no = int(input("Enter other user account number : "))
        other_user = exist_account(other_account_no)

        if user_account_no == other_account_no:
            print("Account Number always unique...")
        elif user == True and other_user == True:
            transfer_balance = int(input("Enter amount : "))
            if transfer_balance > 0:
                transfer_money(user_account_no,
                               other_account_no, transfer_balance)
            else:
                print("Amount should be positive...")
        else:
            print("Enter correct account number...")

    elif operation == 6:
        break

    else:
        print("Number does not match")
