# The open() function takes two parameters; filename, and mode
#          modes:
# "r" - Read -  Opens a file for reading
# "a" - Append - Открывает файл для сложения
# "w" - Write 
# # "x" - Create - Creates the specified file

""" "t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)"""


f = open('TSIS-6/demofile.txt', 'r')
print(f.read())
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.


# Read Only Parts of the File
f = open('TSIS-6/demofile.txt', 'rt')
print(f.read(6))

# Read Lines
f = open('TSIS-6/demofile.txt', 'rt')
print(f.readline())
print(f.readline())

f =open('TSIS-6/demofile.txt' , 'r')
for x in f :
    print(x)
f.close()

# Write to an Existing File
f = open("TSIS-6/demofile.txt", "a")
f.write("Fariza")
f.close()

#open and read the file after the appending:
f = open("TSIS-6/demofile.txt", "r")
print(f.read())

f = open("demofile2.txt" , "w")
f.write("My name is Fariza")
f.close()
f = open("demofile2.txt" , "r")
print(f.read())

# Create a New File
f = open("newFile.txt" , "w")
f.write("fariza did it")
f.close()
f = open("newFile.txt" , "r")
print(f.read())

# Delete a File
f = open("exaples/demofile.txt" , "r")
import os
os.remove("exaples/demofile.txt")

# Check if File exist:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# Delete Folder /Чтобы удалить всю папку, используйте метод os.rmdir():
  import os
os.rmdir("myfolder")
