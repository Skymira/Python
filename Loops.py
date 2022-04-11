i = 1
# i will multiply *
while i<=5:
    print('*'* i)
    i += 1
print("Done")


#Guessing game project
hidden_number = 9
guess_number = 0
number_of_tries = 0
while guess_number != hidden_number:
    if number_of_tries < 3:
        guess_number = input("Guess: ")
        guess_number = int(guess_number)
        number_of_tries += 1
    else:
        print(f"You lost, tries: {number_of_tries}")
        break
if guess_number == hidden_number:
        print(f"You won, tries: {number_of_tries}")


