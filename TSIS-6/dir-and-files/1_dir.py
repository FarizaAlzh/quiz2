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

