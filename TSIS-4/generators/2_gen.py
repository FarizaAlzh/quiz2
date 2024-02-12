# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
n = int(input())
def even(n):
    for i in range(n):
        if i%2==0:
            yield i 
even_string = ",".join(str(num) for num in even(n))
print(even_string)

# yield для возврата значений
# Это цикл, который проходит по каждому элементу, возвращаемому генератором even(n).

# разделитель.join(последовательность)
# объединяет элементы последовательности в одну строку, разделяя их указанным разделителем