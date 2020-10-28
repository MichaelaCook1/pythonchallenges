
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    class_="student"

    def average(self,score1,score2,score3):
        total = score1 +score2+ score3
        avg=total/3
        return avg
    


John = Student("John", "21")
Jane = Student("Jane", "22")
print(getattr(John, "age"))
Jake = Student("Jake",23)
print(Jake.class_)
print(Jake.average (60,65,70))