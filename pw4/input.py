from domain import Student, Course, Mark
from manage import create_marksheet, find_course, find_student, edit_mark


def input_student(s):
    i = input("Enter a number of student(s): ")
    try:
        n = int(i)
    except ValueError:
        print("This is not a valid input")
    else:
        if n <= 0:
            print("This is not a valid input")
        else:
            for j in range(n):
                ID = input("Enter student ID: ")
                find = False
                for k in range(len(s)):
                    if ID == s[k].returnID():
                        Name = input("Enter student Name: ")
                        Dob = input("Enter student DoB: ")
                        s[k].setName(Name)
                        s[k].setDob(Dob)
                        find = True
                        break
                if find == False:
                    Name = input("Enter student Name: ")
                    Dob = input("Enter student DoB: ")
                    print("")
                    s.append(Student(ID,Name,Dob))

# s should be a list of students
def input_course(c, s):
    i = input("Enter a number of course(s): ")
    try:
        n = int(i)
    except ValueError:
        print("This is not a valid input")
    else:
        if n <= 0:
            print("This is not a valid input")
        else:
            for j in range(n):
                ID = input("Enter course ID: ")
                find = False
                for k in range(len(c)):
                    if ID == c[k].returnID():
                        find = True
                        Name = input("Enter course Name: ")
                        Credits = input("Enter course Credits: ")
                        try:
                            n = int(Credits)
                        except ValueError:
                            print("This is not a valid input")
                            return
                        else:
                            if n <= 0:
                                print("This is not a valid input")
                                return
                        c[k].setName(Name)
                        c[k].setCredits(Credits)
                        break
                if find == False:
                    Name = input("Enter course Name: ")
                    Credits = input("Enter course Credits: ")
                    try:
                        n = int(Credits)
                    except ValueError:
                        print("This is not a valid input")
                        return
                    else:
                        if n <= 0:
                            print("This is not a valid input")
                            return
                    Marksheet = []
                    check = create_marksheet(Marksheet, s)
                    if check == 0:
                        print("Marksheet create unsuccessful")
                        print("Exception found")
                        return
                    else: 
                        print("Marksheet created successful")
                        c.append(Course(ID,Name,Marksheet, Credits))
                    print("")

def input_MarkOfStudentInCourse(c, s):
    course = find_course(c)
    if course == None:
        return
    else:
        student = find_student(s)
        if student == None:
            return
        else:
            check = False
            for i in range(len(course.Marksheet)):
                if course.Marksheet[i].getStudent() == student:
                    print("Student in course found")
                    check = True
                    a, m, f = edit_mark()
                    if a == None:
                        return
                    else:
                        course.Marksheet[i].setMark(a,m,f)
                        print("")
            if check == False:
                print("Student not in course")