#Get Student List
def input_students(students=[]):
    a = int(input("Enter the number of student(s): "))
    print("")
    for i in range(a):
        name = input("Enter the name of the student: ")
        id = input("Enter the id of the student: ")
        dob = input("Enter the date of birth of the student (DD/MM/YYYY): ")
        print("")
        students.append({"Name": name, "Student ID": id, "DoB": dob})
    return students
# Get Course list
def input_course(course = []):
    a = int(input("Enter the number of course(s): "))
    for i in range(a):
        name = input("Enter the name of the course: ")
        id = input("Enter the id of the course: ")
        mark = {"Student ID": "", "Midterm": "", "Final": ""}
        print("")
        course.append({"Name": name, "Course ID": id, "mark": mark})
    return course
# Input mark
def input_mark(students, course):
    a = input("Enter the ID of the student: ")
    b = input("Enter the ID of the course: ")
    a_true = False
    b_true = False
    for i in range(len(course)):
        if course[i]["Course ID"] == b: #Check if course exist
            b_true = True
            for j in range(len(students)):
                if students[j]["Student ID"] == a: #Check if student exist
                    a_true = True
                    course[i]["mark"]["Student ID"] = a
                    course[i]["mark"]["Midterm"] = input("Enter the Midterm of the student: ")
                    #Check if the mark is valid
                    if float(course[i]["mark"]["Midterm"]) >= 0 and float(course[i]["mark"]["Midterm"]) <= 20:
                        print("Thank you")
                    else:
                        print("The mark must be between 0 and 20")
                        course[i]["mark"]["Midterm"] = input("Enter the Midterm of the student: ")
                    course[i]["mark"]["Final"] = input("Enter the Final of the student: ")
                    #Check if the mark is valid
                    if float(course[i]["mark"]["Final"]) >= 0 and float(course[i]["mark"]["Final"]) <= 20:
                        print("Thank you")
                    else:
                        print("The mark must be between 0 and 20")
                        course[i]["mark"]["Final"] = input("Enter the Final of the student: ")
                    print("")
                elif j == len(students) - 1 and a_true == False:
                    print("Student ID is not found")
                    print("")
        elif i == len(course) - 1 and b_true == False:
            print("Course ID is not found")
            print("")
def print_students(students):
    print(students)
def print_course(course):
    print(course)
def print_mark_all(course):
    for i in range(len(course)):
        print(course[i]["mark"])
def print_mark_student(course, students):
    a_true = False
    b_true = False
    a = input("Enter the ID of the student that you want to see: ")
    b = input("Enter the ID of the course that you want to see: ")
    for i in range(len(course)):
        if course[i]["Course ID"] == b: #Check if course exist
            b_true = True
            for j in range(len(students)):
                if students[j]["Student ID"] == a: #Check if student exist
                    a_true = True
                    print("Name: " + students[j]["Name"])
                    print("Midterm: " + course[i]["mark"]["Midterm"])
                    print("Final: " + course[i]["mark"]["Final"])
                    print("")
                elif j == len(students) - 1 and a_true == False:
                    print("Student ID is not found")
                    print("")
        elif i == len(course) - 1 and b_true == False:
            print("Course ID is not found")
            print("")
def main(): #Test all functions
    students = input_students()
    course = input_course()
    input_mark(students, course)
    print_students(students)
    print_course(course)
    print_mark_all(course)
    print_mark_student(course, students)
main() 
