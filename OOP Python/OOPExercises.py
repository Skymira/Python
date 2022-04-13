class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Hi, I am "+self.name)

person = Person("John")
#print(person.name)
person.talk()
bob = Person("Bob")
bob.talk()