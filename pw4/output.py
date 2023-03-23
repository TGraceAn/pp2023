from manage import find_course, find_student

def find_MarkOfStudentInCourse(c, s):
    course = find_course(c)
    if course == None:
        return
    else:
        student = find_student(s)
        if student == None:
            return
        else:
            course.getMark(student)

def list_AllStudents(s):
    for i in range(len(s)):
        s[i].getInfo()
        print("")

def list_AllCourses(c):
    for i in range(len(c)):
        c[i].getInfo()
        print("")

def find_GPA_Student(s):
    student = find_student(s)
    if student == None:
        return
    else:
        student.getGPA()

def showMarksheet(c):
    course = find_course(c)
    if course == None:
        return
    else:
        for i in range(course.Marksheet):
            course.Marksheet[i].getMark()