import textwrap
import numpy as np
import curses
import math
# IDEA
# Create 3 classes, student, course and mark

# Functions
# List of courses, each course has a marksheet with is a list of marks for each students




#CLASSES
#tbh idk what i will use this for, but yeah, fun inheritance, lol
class info:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def getinfo(self):
        print(self.id)
        print(self.name)

#template to create students // HAHAHAHAH I CREATE PEOPLE
class student(info):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob
        self.GPA = 1000
    def getinfo(self):
        super().getinfo()
        print(self.dob)
    #get mark of a course
    def getmark(self, c):
        i = False
        while i == False:
            for i in range(len(c.marksheet)):
                if c.marksheet[i].student.id == self.id:
                    c.marksheet[i].getmark()
                    i = True
                    break 
        if i == False:
            print("Error")
    def getGPA(self):
        print(f"GPA of {self.id} _ {self.name}: ")
        print(self.GPA)
        return self.GPA
    def __lt__(self, other):
        return self.getGPA() < other.getGPA()
        
#course has a marksheet, marksheet has a list of students
class course(info):
    def __init__(self, id, name, marksheet, credits):
        super().__init__(id, name)
        self.marksheet = marksheet
        self.credits = credits
    def getinfo(self):
        super().getinfo()
        for i in range(len(self.marksheet)):
            self.marksheet[i].getmark()

#mark is for a student
class mark():
    def __init__(self, student, mid, final):
        self.student = student
        self.mid = mid
        self.final = final
        self.overall = math.floor((20*0.1 + mid*0.35 + final*0.55)*10)/10
    def getmark(self):
        print(f"{self.student.id} _ {self.student.name}")
        print(f"Mid: {self.mid}")
        print(f"Final: {self.final}")




#FUNCTIONS
#get student list // s here is a list of object students
def input_students(s):
    n = int(input("Enter the number of student(s): "))
    while n <= 0:
        print("Invalid number of students")
        n = int(input("Enter the number of student(s): "))
    for i in range(n):
        id = input("Enter the id of the student: ")
        name = input("Enter the name of the student: ")
        dob = input("Enter the date of birth of the student (DD/MM/YYYY): ")
        print("")
        s = np.append(s, student(id,name,dob))
    return s

#Get list of courses, s should be a list of students
def input_courses(c,s):
    n = int(input("Enter the number of course(s): "))
    while n <= 0:
        print("Invalid number of courses")
        n = int(input("Enter the number of course(s): "))
    for i in range(n):
        id = input("Enter the id of the course: ")
        name = input("Enter the name of the course: ")
        credits = int(input("Enter the credits of the course: "))
        m = []
        marksheet = create_marksheet(m,s)
        print("")
        c.append(course(id, name, marksheet, credits))

def input_midterm():
    n = float(input("Enter mark for midterm: "))
    while n < 0 or n > 20:
        print("Invalid mark")
        n = float(input("Enter mark for midterm: "))
    return n
    
def input_final():
    n = float(input("Enter mark for final: "))
    while n < 0 or n > 20:
        print("Invalid mark")
        n = float(input("Enter mark for midterm: "))
    return n

#input marks for a student --> return a mark object
def input_marks(student):
    n = input_midterm()
    m = input_final()
    return mark(student,n,m)

#s should be a list of students
def create_marksheet(m,s):
    for i in range(len(s)):
        print(f"Input the mark for: {s[i].id} _ {s[i].name}")
        m.append(input_marks(s[i]))
    return m


#to display all students
def student_interface(s):
    for i in range(len(s)):
        s[i].getinfo()
        print("")

#to display all courses
def course_interface(c):
    for i in range(len(c)):
        c[i].getinfo()
        print("")

#to display marksheet for a given course
def marksheet_interface(c):
    for i in range(len(c.marksheet)):
        c.marksheet[i].getmark()
        print("")

#Add more mark of students into marksheet
def update_marksheet(marksheet,s):
    for i in range(len(s)):
        found = False
        for j in range(len(marksheet)):
            if s[i] == marksheet[j].student:
                found = True
                break
        if found == False:
            print(f"Input the mark for: {s[i].id} _ {s[i].name}")
            n = input_midterm(s[i])
            m = input_final(s[i])
            marksheet.append(mark(s[i],n,m))

def GPA_sort(s):
    s.sort(reverse = True)

def calGPA(c):
    total_score = 0
    num_cre = 0
    for i in range(len(c)):
        for j in range(len(c[i].marksheet)):
            if c[i].marksheet[j].student.id == id:
                total_score += c[i].marksheet[j].overall * c[i].credits
                num_cre += c[i].credits
    GPA = math.floor((total_score/num_cre)*10)/10
    c[i].marksheet[j].student.GPA = GPA

#MAIN
def main():
    print("Welcome! ")
    s = np.array([])
    c = []
    #c = np.array([])
    while True:
        print(textwrap.dedent("""
        What else do you want to do?
            1- Add more students
            2- Add more courses
            3- Add/Change mark of a student in a course
            4- Show marksheet of a course
            5- Display all students info
            6- Show all courses info
            7- Add new students to a course
            8- Cal GPA of all students
            9- Show GPA of a student
            10- Sort student by GPA
            11- Exit
        """))
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                s = input_students(s)
            case 2:
                input_courses(c,s)
            case 3:
                while True:
                    print(textwrap.dedent("""
                        Choose your way of finding
                            1- Find course using course ID:
                            2- Find course using course Name:
                            3- Exit """))       
                    option = int(input("Option: "))
                    match option:
                        case 1:
                            newID = input("Enter the course ID: ")
                            find_course = False
                            for i in range(len(c)):
                                if c[i].id == newID:
                                    find_course = True
                                    find_student = False
                                    new_new_ID = input("Enter student ID: ")
                                    for j in range(len(c[i].marksheet)):
                                        if c[i].marksheet[j].student.id == new_new_ID:
                                            find_student = True
                                            input_marks(c[i].marksheet[j].student)
                                            break
                                    if find_student == False:
                                        print("Sorry, I can't do that")
                                    break
                            if find_course == False:
                                print("Sorry, I can't do that")
                            break
                        case 2:
                            newName = input("Enter the course name: ")
                            find_course = False
                            for i in range(len(c)):
                                if c[i].name == newName:
                                    find_course = True
                                    find_student = False
                                    new_new_ID = input("Enter student ID: ")
                                    for j in range(len(c[i].marksheet)):
                                        if c[i].marksheet[j].student.id == new_new_ID:
                                            find_student = True
                                            input_marks(c[i].marksheet[j].student)
                                            break
                                    if find_student == False:
                                        print("Sorry, I can't do that")
                                    break
                            if find_course == False:
                                print("Sorry, I can't do that")
                            break
                        case 3:
                            break
            case 4:
                while True:
                    print(textwrap.dedent("""
                        Choose your way of finding
                            1- Find course using course ID:
                            2- Find course using course Name:
                            3- Exit """))      
                    option = int(input("Option: "))
                    match option:
                        case 1:
                            newID = input("Enter the course ID: ")
                            find_course = False
                            for i in range(len(c)):
                                if c[i].id == newID:
                                    find_course = True
                                    marksheet_interface(c[i])
                                    break
                            if find_course == False:
                                print("Sorry, I can't do that")
                            break
                        case 2:
                            newname = input("Enter the course name: ")
                            find_course = False
                            for i in range(len(c)):
                                if c[i].name == newname:
                                    find_course = True
                                    marksheet_interface(c[i])
                                    break
                            if find_course == False:
                                print("Sorry, I can't do that")
                            break
                        case 3:
                            break
            case 5:
                student_interface(s)
            case 6:
                course_interface(c)
            case 7:
                while True:
                    print(textwrap.dedent("""
                        Choose your course
                            1- Find course using course ID:
                            2- Find course using course Name:
                            3- Exit """))      
                    option = int(input("Option: "))
                    match option:
                        case 1:
                            newID = input("Enter the course ID: ")
                            find_course = False
                            for i in range(len(c)):
                                if c[i].id == newID:
                                    find_course = True
                                    update_marksheet(c[i].marksheet,s)
                                    break
                            if find_course == False:
                                print("Sorry, I can't do that")
                            break
                        case 2:
                            newname = input("Enter the course name: ")
                            find_course = False
                            for i in range(len(c)):
                                if c[i].name == newname:
                                    find_course = True
                                    update_marksheet(c[i].marksheet,s)
                                    break
                            if find_course == False:
                                print("Sorry, I can't do that")
                            break
                        case 3:
                            break
            case 8:
                for k in range(len(s)):
                    total_score = 0
                    num_cre = 0
                    for i in range(len(c)):
                        for j in range(len(c[i].marksheet)):
                            if c[i].marksheet[j].student.id == s[k].id:
                                total_score += c[i].marksheet[j].overall * c[i].credits
                                num_cre += c[i].credits
                    GPA = math.floor((total_score/num_cre)*10)/10
                    s[k].GPA = GPA
            case 9:
                while True:
                    print(textwrap.dedent("""
                        Choose your way of finding student
                            1- Find student using student ID:
                            2- Find studetn using student Name:
                            3- Exit """))      
                    option = int(input("Option: "))
                    match option:
                        case 1:
                            newID = input("Enter the student ID: ")
                            find = False
                            for i in range(len(s)):
                                if s[i].id == newID:
                                    find = True
                                    s[i].getGPA()
                                    break
                            if find == False:
                                print("Sorry, I can't do that")
                        case 2:
                            newName = input("Enter the student Name: ")
                            find = False
                            for i in range(len(s)):
                                if s[i].name == newName:
                                    find = True    
                                    s[i].getGPA()
                                    break
                            if find == False:
                                print("Sorry I can't do that")
                        case 3:
                            break
            case 10:
                GPA_sort(s)
            case 11:
                break


main()

#TODO: 
# change s from list to np.array and still works done


# decorate with curses
