class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("what ur name da?")
        self.name=name

class Student(Wizard): #Wizard is the superclass and Student and Professor are the subclasses
    def __init__(self,name, house):
        super().__init__(name) # way of programmatically acssesing the current class's superclass's methods
        self.house=house

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name) # calling the superclass ka init method
        self.subject=subject

wizard=Wizard("Albus Dumbledore")
student=Student("Harry","Gryffindor")
professor=Professor("Snape", "Potions")

#exceptios are all like inherited from aother base exception