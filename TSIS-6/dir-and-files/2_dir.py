# Ex 6
import string

def gen_files():
    alphabet = string.ascii_uppercase
    for letter in alphabet:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")

gen_files()

# EX 7 Write a Python program to copy the contents of a file to another file
with open('TSIS-6/exaples/demofile2.txt', 'r') as file1, open('TSIS-6/exaples/newFile.txt', 'a') as file2:
  for line in file1:
    file2.write(line)

# EX 8
import os
path = 'X.txt'
path_bool = os.access(path, os.F_OK) #проверяет существование файла

if path_bool == False:
    print("Не существует")
    
elif path_bool == True:
    os.remove(path)
    print("Удален")
