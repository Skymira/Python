is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")


print("Enjoy your day")

price = 1000000
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


has_high_income = True
has_good_credit = True
has_criminal_record = False

# works with [and, or]
#if has_high_income and has_good_credit:
   # print("Eligible for load")
#else:
   # print("Not eligible for loan")

#and not operator
if has_good_credit and not has_criminal_record:
        print("Yes")


temperature = 31

if temperature > 30:
    print("Hot")
elif temperature < 10:
    print("Cold")
else:
    print("Normal")

#Exercise
name = "Jack"
name_char = len(name)
if name_char < 3:
    print("Name must be at least 3 characters")
elif name_char > 50:
    print("Name can be max of 50 characters")
else:
    print("Great name")

#Exercise
user_weight = input("Weight: ")
user_weight_type = input("(L)bs or (K)g: ")
user_weight = int(user_weight)
if user_weight_type.upper() == "L":
    weight_converted = user_weight / 2.205
    print(f"You are: {weight_converted} kilo")
elif user_weight_type.upper() == "K":
    weight_converted = user_weight * 2.205
    print(f"You are: {weight_converted} pounds")
else:
    print("Wrong unit")