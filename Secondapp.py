import math;
# importing math functions
math.ceil(2.9);
# ceil puts your number to top (3)
math.floor(2.9)
# floor drops it down (2)


#How many times 3 goes to 10
print(10 // 3);
print(10 % 3);

#10 to power 3
print(10 ** 3);

#Incrementing a number
x = 10;
x = x + 3;
x += 3
print(x);

# 16
x = 10 + 3 *2;
print(x);

#Order of operations
# PARENTHESIS ALWAYS TAKES THE PRIORITY
# 1) exponentiation 2**3
# 2) multiplication or division
# 3) addition or substraction
x = 10 + 3 * 2 ** 2;
print(x);
x = (10 + 3) * 2 ** 2;
print(x);

x = (2 + 3) * 10 - 3;
print(x);

#round function will change 2.9 to 3
# and from 2.4 it will drop it to down 2
y = 2.9;
print(round(y));

#absolute value
#Always gonna return positive value
print(abs(-2.9));
