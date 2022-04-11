print("Hello World");
print("o----");
print(" ||||");
print("*" * 10);
#executes line by line so price will be 20
price = 10;
price = 20;
rating = 4.9;
#Exercise1
full_name = "Jonh Smith";
age = 20;
is_new = True;
##################
#needs to be written Uppercase letter True/False and variable must be small
is_published = True;
print(price);
#Take input
#Exercise2
name = input("What is your name? ");
color = input("What is your fav. color? ");
print(name+" likes "+color);

birth_year = input("Birth year: ");

#check the type of variable
print(type(birth_year));

#convert string to int
age = 2022 - int(birth_year);
print(age);

#Exercise3
user_weight = input("What is your weight(in pounds)? ");
weight_kilograms = float(user_weight) /  2.205;
print(weight_kilograms);

#Strings in python
course = "Python's for beginners";
print(course);
course2 = 'Python for "beginners"';
course3 = '''
Hi John,

Here is our first email to you.

Thank you,
The support team
''';

#Getting index of Stringsssssssssssss
course4 = "Python for Beginners";
print(course4[0]);

# -1 is gonna print one index backwards of 0 which in fact is last letter of the string 's'
print(course4[-1]);

#Taking indexs from 0 to 3 but doesnt return the letter under the 3rd index
#pyt
# If you dont specify the second index Python will return all the indexs to the end
print(course4[0:3]);

#This variable is gonna be a copy of the course variable
another = course4[:];

#Formatted Strings
first = "John";
last = "Smith";
message = first + " ["+last +"] is a coder";

#Curly brackets define a hole in our formated String
#So we can put them without concatating them "+"
#We use f before it to define a formatted String
msg = f'{first} [{last}] is a coder';
print(message);
print(msg);

#String methods
course5 = "Python for Beginners";
print(len(course5));
#Convert to upper case
# lower - to lower case
print(course5.upper());
# Only the above line will be affected by . upper
# next time we print course5 it will be in its normal state

#Returns index of given character
#Sensitive to lower case
print(course5.find('P'));

#Replaces to word beinners to absolute beginners
print(course5.replace("Beginners","Absolute Beginners"));

#Check if String exists in variable course5
#Returns true/false
print("Python" in course5);

#Prints itself
print(course5.title());