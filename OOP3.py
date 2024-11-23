
class Student():
    @classmethod
    def get(cls):
        name=input("Enter name: ")
        house=input("Enter house: ")
        return cls(name,house)
    #rhis is crazy, coz u are rurtun basically 2 things but whats with the syntax?
    # so line 47 means, create an object of the current class (whatever cls is) and retrun that
    #this returns the called object to every 'self' argument
    #so everywhen self is called, this """  cls(name,house) """ is supplied to it

    def __init__(self,name,house):
        self.name=name
        self.house=house

    def __str__(self): #returns the object as a string, only takes in one argument, self
        return f"{self.name} is in {self.house}"

def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

