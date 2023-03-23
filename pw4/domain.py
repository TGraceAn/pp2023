from math import floor

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