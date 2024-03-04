# EX 1
# Write a Python program to list only directories, files and all directories, files in a specified path.
import os # для взаимодействия с операционной системой
# перечислить только каталоги, файлы и все каталоги, файлы в указанном пути.
path = input("каталог: ")

def list_dir_file(path):
    print("\nКаталоги:")
    for name in os.listdir(path):    #проверяет,является ли текущий элемент каталогом
        if os.path.isdir(os.path.join(path, name)): #os.path.join() объединяет указанные части пути вместе, чтобы создать полный путь. 
            print(name)                             #создания полного пути к текущему каталогу

    print("\nФайлы:")
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            print(name)

def list_all_dir_file(path):
    print("\nСписок всех каталогов:")
    for root, dirs, files in os.walk(path):  # перебрать все файлы в указанном пути
        for dir_name in dirs:
            print(os.path.join(root, dir_name))

    print("\nСписок всех файлов:")
    for root, dirs, files in os.walk(path): # католог который мы рассматриваем 
        for file_name in files:
            print(os.path.join(root, file_name))


list_dir_file(path)
print("\nСписок всех каталогов и файлов:")
list_all_dir_file(path)

# TSIS-6


# EX 2
if os.path.exists(path): 
    print("The path exists")
else:
    print("The path does not exist")

if os.access(path, os.R_OK): #доступно ли чтение
    print("You can read the path")
else:
    print("Unable to read path")

if os.access(path, os.W_OK):
    print("Can be write")
else:
    print("Unable to write")

if os.access(path, os.X_OK):
    print("You can follow the path")
else:
    print("Unable to execute path")


# EX 3
if os.path.exists(path):
    dir, file = os.path.split(path)
    print(f"File name: {file}")
    print(f"Part of the catalog: {dir}")
else:
    print("The specified path does not exist.")

# EX 4 
with open(r"TSIS-6/exaples/demofile.txt", 'r') as file:
    lines = len(file.readlines())
    print('Number of lines:', lines)

# EX 5 
list = ['Fariza', 'Adal', 'Sultan']

with open('TSIS-6/exaples/demofile.txt' , 'w') as file:
    for i in list:
        file.write(i + '\n')
file.close()

