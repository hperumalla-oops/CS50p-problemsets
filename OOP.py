#u can import classes
class Student:
    def __init__(self,a,b): #convention you call it slef otherwise u can call it anything u feel like but the first arg is the self reference one
                            # also for optional arguments b=None ie default is None, so it not req mandatorily by user.
                             ##### whats the diff between a function and a method?
                              ###OK WHEN A  fucntion is bulit into a class its called method- methods always take in atleast one argument - self -
        if not a:
            raise ValueError("Missing Name") # can raise an error when some random unexcpected shit happens
                                            # note error has to exist prvly but u can make up ur own error as another class or smg
        ##### CODE if b not in ["G","H","R","S"]:
            #### CODE raise ValueError("Invalid House u suck loserrrrrr")
        self.name=a
        self.house=b   # this will aslo call the setter method 'self.house=' this itself (attribut+assignment operator) is an enuf indicator to call setter func
                        # here we dont use _house coz then it will pass thru the setter .house id the only thing that setter looks for
    def __str__(self):   #basically helps in returning the object as a string, only takes in one argument self
        return f"{self.name} from {self.house}"

    @property #getter:
    def house(self):
        return self._house  #cannot have function and instance variable with the same name

    @house.setter #setter # to say here comes a function whose nmae is identical but 2 arg
    def house(self, b):
        if b not in ["G","H","R","S"]:
            raise ValueError("Invalid House u suck loserrrrrr")
        self._house=b
        #name and house will be you return values
        #a,b will be the input data that require storing
        # like a,b are stored in name, house

def main():
    student = get_name()
    #print(f"{student.name} from {student.house}")
    print(student)
    student.house="loser"
    # so the blueprint of a defined class Student has to always be passed onto a variable or can we call it chuma?

def get_name():
    #student= Student()
    name=input("name: ")
    house=input("house: ")
    return Student(name,house)   #constructor code = it is going to construct a student object for me.
    # AKA its going to instantiate the student object for me


if __name__ == "__main__":
    main()