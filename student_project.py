students = [
    {"id": 1, "name": "Suman", "age": 24, "marks": [80, 75, 90]},
    {"id": 2, "name": "Pritam", "age": 30, "marks": [90, 70, 92]},
    {"id": 3, "name": "Rahul", "age": 25, "marks": [90, 76, 90]},
    {"id": 4, "name": "Saikat", "age": 26, "marks": [93, 76, 92]},
    {"id": 5, "name": "Souvik", "age": 22, "marks": [80, 70, 92]}
]


def add_student(student_id, student_name, student_age, student_marks):

    final_dict = {}

    final_dict["id"] = student_id
    final_dict["name"] = student_name
    final_dict["age"] = student_age
    final_dict["marks"] = student_marks

    students.append(final_dict)
    print(f"Student details : {final_dict}")
    print(f"All students details : {students}")


def search_student(student_id):

    for my_dict in students:
        id = my_dict["id"]
        if id == student_id:
            print(my_dict)
            break
    else:
        print("Student not found")


def update_student(student_id, student_name, student_age, student_marks):

    for my_dict in students:
        id = my_dict["id"]

        if id == student_id:
            my_dict["name"] = student_name
            my_dict["age"] = student_age
            my_dict["marks"] = student_marks
            print("Student Id can not be changed ")
            print(f"Updated student details : {my_dict}")
            print(f"All students details : {students}")
            break


def delete_student(student_id):

    for my_dict in students:
        id = my_dict["id"]
        if id == student_id:
            students.remove(my_dict)
            print(f"All students details : {students}")
            break


def average_marks(student_id):

    for my_dict in students:
        id = my_dict["id"]
        list_marks = my_dict["marks"]
        if id == student_id:
            average = sum(list_marks) / len(list_marks)
            rounded_num = round(average, 2)
            print(rounded_num)
            break


def highest_score():

    total_average = {}
    for my_dict in students:
        id = my_dict["id"]
        name = my_dict["name"]
        marks = my_dict["marks"]
        average_marks = sum(marks)/len(marks)
        round_marks = round(average_marks, 2)
        total_average[id] = [name, round_marks]

    highest_average_marks = 0
    name = ""
    for key, value in total_average.items():
        if total_average[key][1] > highest_average_marks:
            highest_average_marks = total_average[key][1]
            name = total_average[key][0]
            id = key
    print("id :", id, ", name :", name,
          ", highest_average_marks :", highest_average_marks)


def valid_id():
    while True:
        try:
            user_input = int(input("Enter student ID :"))
            return user_input
        except ValueError:
            print("Invalid input! ID must be integer...")


def valid_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if 20 <= age <= 40:
                return age
            else:
                print("Enter age in the 20 - 40 range")

        except ValueError:
            print("Enter a valid age inside the range (20 - 40)")


def valid_marks():
    while True:
        try:
            marks = []
            for i in range(3):
                mark = int(input("Enter marks: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                else:
                    print("Marks must be between 0 and 100.")
                    break
            else:
                return marks

        except ValueError:
            print("Invalid marks! Marks must be an integer.")


def id_exist(student_id):

    for my_dict in students:
        id = my_dict["id"]
        if id == student_id:
            return True
    else:
        return False


while True:
    try:
        user_input = int(input(
            "Select an operation:\n"
            "Press 1: Add a student\n"
            "Press 2: Search for a student\n"
            "Press 3: Update student details\n"
            "Press 4: Delete a student\n"
            "Press 5: Calculate the average score of a student\n"
            "Press 6: Find the highest score\n"
            "Press 7: Exit the loop\n"
            "Enter your choice: "
        ))

        if user_input == 1:
            id = valid_id()

            id_value = id_exist(id)
            if id_value != True:
                name = input("Enter student name :")
                age = valid_age()
                marks = valid_marks()
                add_student(id, name, age, marks)
            else:
                print("ID already exist")

        elif user_input == 2:
            id = valid_id()
            search_student(id)

        elif user_input == 3:
            id = valid_id()

            id_value = id_exist(id)
            if id_value == True:
                name = input("Enter student name :")
                age = valid_age()
                marks = valid_marks()
                update_student(id, name, age, marks)
            else:
                print("Enter correct ID")

        elif user_input == 4:
            id = valid_id()

            id_value = id_exist(id)
            if id_value == True:
                delete_student(id)
            else:
                print("Student ID does not exist...")

        elif user_input == 5:
            id = valid_id()

            id_value = id_exist(id)
            if id_value == True:
                average_marks(id)
            else:
                print("student Id does not found")

        elif user_input == 6:
            highest_score()

        elif user_input == 7:
            break

        else:
            print("Please enter a correct number...")
    except ValueError:
        print("Please Enter a valid input")
