class Actor:
    def XXX():
        UsosWebPage().show()


class UsosWebPage:
    def show(self):
        GradeController(self.student).getStudentGradeInfo()


class GradeController:
    def __init__(self, student):
        self.student = student

    def getStudentGradeInfo(self):
        courses = self.student.getCourses()
        marks = []
        for course in courses:
            mark = course.getMark(self.student)
            marks.append(mark)
        return marks


class Student:
    def __init__(self, index):
        self.index = index

    def getCourses(self):
        pass


class Course:
    def getMark(self, student):
        self.getValue(student.index)

    def getValue(self, index):
        pass
