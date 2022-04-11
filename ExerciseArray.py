#Removing duplicates from list

numbers = [1, 1, 2, 2, 5, 6, 6, 1, 8, 9, 9, 1, 2, 4, 8]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)


# We cannot change tuples
# they are defined by ()
numberss = (1, 2, 3)
print(numberss[0])


coordinates = (1, 2, 3)

#Called unpacking can be used on lists also
#same as below
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]


# same as above
x,y,z = coordinates

