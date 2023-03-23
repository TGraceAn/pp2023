from domain import Student, Course, Mark

def find_course(c):
    check = input("Enter course ID: ")
    find = False
    for i in range(len(c)):
        if c[i].returnID() == check:
            print("Course found!")
            find = True
            return c[i]
    if find == False:
        print("Course not found")

def find_student(s):
    check = input("Enter student ID: ")
    find = False
    for i in range(len(s)):
        if s[i].returnID() == check:
            print("Student found!")
            find = True
            return s[i]
    if find == False:
        print("Student not found")

# c is a course, s is a list of students
def Update_single_student(c, s):
    student = find_student(s)
    if student == None:
        return
    else:
        check = False
        for i in range(len(c.Marksheet)):
            if c.Marksheet[i].getStudent() == student:
                print("Student already in course")
                check = True
                return
        if check == False:
            mark = input_mark(student)
            c.Marksheet.append(mark)

def Reomove_single_student(c, s):
    student = find_student(s)
    if student == None:
        return
    else:
        check = False
        for i in range(len(c.Marksheet)):
            if c.Marksheet[i].getStudent() == student:
                c.Marksheet.remove(c.Marksheet[i])
                check = True
                return
        if check == False:
            print("Student not in course")

def Update_all_student(c, s):
    course = find_course(c)
    if course == None:
        return
    else:
        for i in range(len(s)):
            found = False
            for j in range(len(course.Marksheet)):
                if s[i] == course.Marksheet[j].getStudent():
                    found = True
                    break
            if found == False:
                mark = input_mark(s[i])
                course.Marksheet.append(mark)
    
#both c and s are lists
def Update_all_students_GPA(c, s):
    for i in range(len(s)):
        s[i].calGPA(c)

def GPA_sort(s):
    s.sort(reverse = True)

#input mark for a give student --> use to create a marksheet
def input_mark(s):
    Attendance = input("Enter mark for Attendance: ")
    try:
        a = float(Attendance)
    except ValueError:
        print("This is not an valid input")
        return 0
    else:
        while a < 0 or a > 20:
            print("This is not an valid input")
            Attendance = input("Enter mark for Attendance: ")
            try:
                a = float(Attendance)
            except ValueError:
                print("This is not an valid input")
                return 0
    Midterm = input("Enter mark for Midterm: ")
    try:
        m = float(Midterm)
    except ValueError:
        print("This is not an valid input")
        return 0
    else:
        while m < 0 or m > 20:
            print("This is not an valid input")
            Midterm = input("Enter mark for Midterm: ")
            try:
                m = float(Midterm)
            except ValueError:
                print("This is not an valid input")
                return 0
    Final = input("Enter mark for Final: ")
    try:
        f = float(Final)
    except ValueError:
        print("This is not an valid input")
        return 0
    else:
        while f < 0 or f > 20:
            print("This is not an valid input")
            Final = input("Enter mark for Final: ")
            try:
                f = float(Final)
            except ValueError:
                print("This is not an valid input")
                return 0
    return Mark(a,m,f,s)

def edit_mark():
    Attendance = input("Enter mark for Attendance: ")
    try:
        a = float(Attendance)
    except ValueError:
        print("This is not an valid input")
        return
    else:
        while a < 0 or a > 20:
            print("This is not an valid input")
            Attendance = input("Enter mark for Attendance: ")
            try:
                a = float(Attendance)
            except ValueError:
                print("This is not an valid input")
                return
    Midterm = input("Enter mark for Midterm: ")
    try:
        m = float(Midterm)
    except ValueError:
        print("This is not an valid input")
        return
    else:
        while m < 0 or m > 20:
            print("This is not an valid input")
            Midterm = input("Enter mark for Midterm: ")
            try:
                m = float(Midterm)
            except ValueError:
                print("This is not an valid input")
                return
    Final = input("Enter mark for Final: ")
    try:
        f = float(Final)
    except ValueError:
        print("This is not an valid input")
        return
    else:
        while f < 0 or f > 20:
            print("This is not an valid input")
            Final = input("Enter mark for Final: ")
            try:
                f = float(Final)
            except ValueError:
                print("This is not an valid input")
                return
    return a,m,f


# create a marksheet for a course, s should be a list of students
def create_marksheet(marksheet, s):
    for i in range(len(s)):
        s[i].getInfo()
        check = input_mark(s[i])
        if check == 0:
            return 0
        else:
            marksheet.append(check)
        print("")
