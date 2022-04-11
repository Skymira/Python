#This is a dictionary
#can add any value/and var
customer = {
    "name": "John Smith",
    "age": 20,
    "is_verified": True
}

#changing name here
customer["name"] = "Jack Smith"
#accessing the dictionary
#case sensitive
print(customer["name"])
#or...
print(customer.get("age"))

#we can define a new thing also

print(customer.get("birthdate","June 19 2000"))