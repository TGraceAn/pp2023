import textwrap
import re
from math import floor
import curses
"""
Idea: Create 3 classes: Courses, Mark and Student
Student has student_info
Course has course_info, each course has a marksheet which has marks for each and every students
Mark has mark of student for each course

"""

#CLASSES
class Info:
    def __init__(self, ID, Name):
        self._ID = ID
        self._Name = Name
    def getInfo(self):
        print(f"{self._ID} _ {self._Name}")
    def returnID(self):
        return self._ID
    def setName(self, NewName):
        self._Name = NewName

class Student(Info):
    def __init__(self,ID,Name,Dob):
        super().__init__(ID,Name)
        self._Dob = Dob
        self._GPA = None
    def getInfo(self):
        super().getInfo()
        print(f"{self._Dob}")
    def calGPA(self, c):
        total_score = 0
        total_credits = 0
        for i in range(len(c)):
            for j in range(len(c[i].Marksheet)):
                if c[i].Marksheet[j].getStudent() == self:
                    total_score += float(c[i].Marksheet[j].returnOverall())*float(c[i].getCredits())
                    total_credits += float(c[i].getCredits())
        self._GPA = floor((total_score/total_credits)*10)/10
    def getGPA(self):
        print(f"{self._ID} {self._Name}")
        print(f"GPA: {self._GPA}")
    def setDob(self, NewDob):
        self._Dob = NewDob
    def returnGPA(self):
        return self._GPA
    def __lt__(self, other):
        return self.returnGPA() < other.returnGPA()
    
class Course(Info):
    def __init__(self, ID, Name, Marksheet, Credits):
        super().__init__(ID, Name)
        self.Marksheet = Marksheet
        self._Credits = Credits
    def getInfo(self):
        super().getInfo()
        print(f"Credits: {self._Credits}")
    def getMark(self, Student):
        find = False
        for i in range(len(self.Marksheet)):
            if self.Marksheet[i].getStudent() == Student:
                find = True
                Student.getInfo()
                self.Marksheet[i].getMark()
                print("")
                break
        if find == False:
            print("Student not found")
    def getCredits(self):
        return self._Credits
    def setCredits(self, Credits):
        self._Credits = Credits
    
class Mark:
    def __init__(self, Attendance , Midterm, Final ,Student):
        self.__Attendance = Attendance
        self.__Midterm = Midterm
        self.__Final = Final
        self.__Student = Student
        self.__Overall = floor(self.__Attendance*10+self.__Midterm*35+self.__Final*55)/100

    def setMark(self, Attendance , Midterm, Final):
        self.__Attendance = Attendance
        self.__Midterm = Midterm
        self.__Final = Final

    def getStudent(self):
        return self.__Student

    def getMark(self):
        self.__Student.getInfo()
        print(f"Attendace: {self.__Attendance}\nMidterm: {self.__Midterm}\nFinal: {self.__Final}\nOverall: {self.__Overall}")

    def returnOverall(self):
        return self.__Overall
    



#INPUT FUNCTIONS

#s should be a list of students
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
    
        


#Managing function
#return course, c should be a list of courses
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




#OUTPUT FUNCTIONS

#Get mark of a student in a course. Both c and s are lists
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

#MAIN
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
                    break
            
        


if __name__ == '__main__':
    main_test()
    