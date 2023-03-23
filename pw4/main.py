import textwrap
from input import input_student, input_course, input_MarkOfStudentInCourse
from output import showMarksheet, list_AllStudents, list_AllCourses, find_MarkOfStudentInCourse, find_GPA_Student
from manage import find_course, Update_all_student, Update_single_student, Reomove_single_student, Update_all_students_GPA, GPA_sort

def main_test():
    print("Welcome")
    s = []
    c = []
    while True:
        print(textwrap.dedent(
            """
            What do you want to do?
                1- Add more students
                2- Add more courses
                3- Add/Change mark of a student in a course
                4- Display marksheet of a course
                5- Display all students info
                6- Display all courses info
                7- Add new students into a course
                8- Update all students into a course
                9- Remove a student from course
                10- Cal GPA of all students
                11- Display GPA of a student
                12- Sort student by GPA
                13- Exit
            """
        ))
        option = input("Enter your option: ")
        try:
            option = int(option)
        except ValueError:
            print("Invalid input")
        else:
            match option:
                case 1:
                    input_student(s)
                case 2:
                    input_course(c, s)
                case 3:
                    input_MarkOfStudentInCourse(c,s)
                case 4:
                    showMarksheet(c)
                case 5:
                    list_AllStudents(s)
                case 6:
                    list_AllCourses(c)
                case 7:
                    i = input("How many students updates? ")
                    try:
                        n = int(i)
                    except ValueError:
                        print("This is not a valid input")
                    else:
                        course = find_course(c)
                        find = True
                        if course == None:
                            print("Can't find course: ")
                            find = False
                        if find == True:
                            for j in range(n):
                                Update_single_student(course,s)
                case 8:
                    Update_all_student(c,s)
                case 9:
                    i = input("How many students updates? ")
                    try:
                        n = int(i)
                    except ValueError:
                        print("This is not a valid input")
                    else:
                        course = find_course(c)
                        find = True
                        if course == None:
                            print("Can't find course: ")
                            find = False
                        if find == True:
                            for j in range(n):
                                Reomove_single_student(c,s)
                case 10:
                    Update_all_students_GPA(c, s)
                case 11:
                    find_GPA_Student(s)
                case 12:
                    Update_all_students_GPA(c, s)
                    GPA_sort(s)
                case 13:
                    find_MarkOfStudentInCourse(c,s)
                case 14:
                    break
            
        


if __name__ == '__main__':
    main_test()