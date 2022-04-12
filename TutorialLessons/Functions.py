#Syntax of function
#Need to call it down
def greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}")
    print('Welcome aboard')


print("Start")
#greet_user("John", "Smith")

#keyword arguments
greet_user(first_name= "John", last_name="Smith")

print("Finished")