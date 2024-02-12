# Implement a generator that returns all numbers from (n) down to 0.
n = int(input())
def generator(n):
    for i in range(n , -1 , -1):
        yield i
for list in generator(n):
    print(list)

# (n , -1 , -1):
    # n = кол чисел 
    # последние число 
    # шаг -1