# it will print all the letters from the string word
# one by one
for item in 'Python':
    print(item)

#It will print all of those strings one by one
for item2 in ['Mosh', 'John', 'Sarah']:
    print(item2)

# will print all ints
for item3 in [1,2,3,4]:
    print(item3)


#Will print all the numbers up to 10
#However 10 is not included
for item4 in range(10):
    print(item4)

#from 5 to 9
for item5 in range(5,10):
    print(item5)


# Will print every second number between 5 and 9
#which is 5 then 7 then 9
for item6 in range(5,10,2):
    print(item6)

#Exercise
prices = [10, 20, 40]
summ = 0
print("Look down below")
for item7 in prices:
    summ = summ + item7

print(summ)




