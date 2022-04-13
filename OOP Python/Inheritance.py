class Mammal:
    def walk(self):
        print("walk")


#dog class inherits Mammal class
#pass means nothing
#it tells python to leave this class empty
class Dog(Mammal):
    pass


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()





