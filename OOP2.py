import random

class Hat:
    def __init__(self):  #self is a required argument to this function(method) called __init__
      self.houses=['A','B','C','D'] # this is an instance variable ie is only defined inside the function(so thats why self ka houses)

    def sort(self, name):
      print(name,"belongs to",random.choice(self.houses))


#intantiate the Hat
 # so now Hat is a class, (lika a datatype kinda) and now a variable needs to be a Hat class ,(like an int class),, we shall call that
hat = Hat() #----> like in my code the variable hat contains within itself the class of Hat (the funtion of Hat)
hat.sort(input("Enter your name ")) #so we are specifically calling the sort method of the class Hat, but this will by default call the init function
# so basically no matter what methhod of the class you call, init is always called

# a clss is a blueprint or template  that allows u to create one or more objects - here hat is an object of class Hat
## when should you use class? --- when u are trying to represent some real world entity




#ok part 2
#sometimes, we dont need to create objects of a class (like hat for Hat over here) , so objects might not even exist
#we can use classes(oject-less) as a container of data or fucntions. This data and fuctionas are somehow related

#instance menthods/variables are defined when that class has an object defined
# and class methods/variables when u dont want/need a any object for that class
#th
class Hat:
     # we can no longer call seld coz we have no object
        houses=['A','B','C','D'] #self.houses was a class method, but now we have only 'houses' which is a class variable
        # there is always only one copy of a class variable, which is shared byt all possible objects that can be created
    @classmethod #like for the class itself,(a funtions whose (one) aregument is the class itself )
    def sort(cls,name): #coz cls=class like how self=object of the class
      print(name,"belongs to",random.choice(cls.houses))


#hat = Hat() #-this like is now unnessesary
Hat.sort(input("Enter your name ")) #capital H
