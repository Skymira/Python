#Day 4 Exercises Car Game

user_input = input("> ")

while user_input.lower() != "quit":
    if user_input.lower() == "start":
        print("Car started...Ready to go!")
        user_input = input("> ")
        if user_input.lower() == "start":
            print("Car is already started!")
            user_input = input("> ")
    if user_input.lower() == "stop":
     print("Car stopped.")
     user_input = input("> ")
     if user_input.lower() == "stop":
        print("Car is already stopped!")
        user_input = input("> ")
    if user_input.lower() == "help":
        print("Start - to start")
        print("Stop - to stop")
        print("Quit - to quit")
        user_input = input("> ")
    else:
        print("I don't understand that")
        user_input = input("> ")




