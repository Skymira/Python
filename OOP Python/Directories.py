import genericpath
from pathlib import Path

#Absolute path
#Relative path

#check if this exists
path = Path("ecommerce")
print(path.exists())


#creates a directory emails
#path1 = Path("emails")
#print(path1.mkdir())

#removes it
#path1.rmdir()

#shows all the py files in current directory
path2 = Path()
for file in path2.glob('*.py'):
    print(file)