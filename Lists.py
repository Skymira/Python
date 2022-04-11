names = ["John", "Bob","Sarah", "Marry"]
print(names[0])

#Updates index 0
names[0] = "Jon"
print(names)
#range of printing index 2 and 3
print(names[2:4])

#Exercise
#Find biggest number of a list
ages = [10, 100, 40]
print(max(ages))

#Other ways
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for i in numbers:
    if max < i:
       max = i
print(max)