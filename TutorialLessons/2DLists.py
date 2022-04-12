#Creating a 2d arrayS
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Accessing values of 2d array
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

numbers = [5, 2, 1, 7, 4]
#Inserting number 10 at given index 0
numbers.insert(0,10)
#adding number to the end of the array
numbers.append(20)

#Removing nr 5
numbers.remove(5)

#It empties the whole array
#numbers.clear()

#Removes last item from the array
numbers.pop();

#shows the index of nr 2
#which is 1
print(numbers.index(2))

#checks if a number exists in this array
print(50 in numbers)

#counting how many times nr1 exists in this array
print(numbers.count(1))

#Sorts the array
numbers.sort()

#Sorts the array in reversed way
numbers.reverse()

#copies our array to another one
numbers2 = numbers.copy()

print(numbers2)

print(numbers)
