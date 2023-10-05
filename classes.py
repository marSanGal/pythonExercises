class Student():
    def __init__(self, name, age, current_class):
        self.name = name
        self.age = age
        self.current_class = current_class
        self.test_scores = []

    def __repr__(self) -> str:
        return f"student name: {self.name}, Student age: {self.age}, Student Class: {self.current_class}"

    def gradeCalc(self, score1, score2, score3):
        return (score1 + score2 + score3)/3

student1 = Student("Hermenegildo", 20, "Maths")
student2 = Student("Benemerita", 16, "Physics")

print(student1.gradeCalc(88,87,56))


from abc import ABC, abstractclassmethod

class Bird(ABC): 
    def __init__(self, fly, colouring):
        self.fly = fly
        self.colouring = colouring

    def __repr__(self) -> str:
        return f"This is different the parent"

    @abstractclassmethod
    def extinct(self):
        pass


class Owl(Bird):
    def __init__(self, fly, colouring, head_rote) -> None:
        super().__init__(fly, colouring)
        self.head_rote = head_rote
    
    def __repr__(self) -> str:
        return f"This is different from the parent"

    
class Dodo(Bird):
    def __init__(self, fly, colouring, ext) -> None:
        super().__init__(fly, colouring)
        self.ext = ext

    def ext(self):
        if self.ext:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"This is different from the parent"

dodo1 = Dodo(False, "Grey", False)

print((dodo1))
    
