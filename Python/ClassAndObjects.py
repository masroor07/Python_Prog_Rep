
#define a class
class Human:
    #define init function, executed when a class is initialised
    #self parameters are used to access various parameters of a class
    def __init__(self, name, age):
        self.name= name
        self.age= age
        #methods are functions belonging to object
    def methods(self):
        print("Hi,my name is", self.name, "and my age is", self.age )
        #passing  objects through the class Human
h1= Human("Masroor",19)
h2= Human("Rahul", 50)
#call for methods
h1.methods()
h2.methods()

'''print(h1.name)
print(h1.age)'''