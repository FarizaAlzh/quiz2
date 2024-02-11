#  Create a generator that generates the squares of numbers up to some number N.
def squares(N):
    for i in range(N):
        yield i ** 2
# yield аналогично ключевому слову return, возвращает значение и "замораживает" состояние функции, чтобы она могла быть возобновлена с последней точки остановки.
# чисел до 10
N = 10
for square in squares(N):
    print(square)

