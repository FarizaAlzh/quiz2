# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
a = int(input())
b = int(input())
def squares(a , b):
    for i in range(a,b):
            yield i*i
for list in squares(a,b):
    print(list)
