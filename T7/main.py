def equals(func):
    def wrapper(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения!")
        return func(self, other)
    return wrapper

def mul_cond(func):
    def wrapper(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы!")
        return func(self, other)
    return wrapper

class Matrix:
    def __init__(self, rows, columns, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    @equals
    def __add__(self, other):
        summa = []
        for i in range(len(self.matrix)):
            row_sum = [self.matrix[i][j] + other.matrix[i][j] for j in range (len(self.matrix[0]))]
            summa.append(row_sum)
        return Matrix(self.rows, self.columns, summa)

    @equals
    def __sub__(self, other):
        sub = []
        for i in range(len(self.matrix)):
            row_sub = [self.matrix[i][j] - other.matrix[i][j] for j in range (len(self.matrix[0]))]
            sub.append(row_sub)
        return Matrix(self.rows, self.columns, sub)

    @mul_cond
    def __mul__(self, other):
        mult = [[0 for _ in range (len(other.matrix[0]))] for _ in range (len(self.matrix))]
        for i in range (len(self.matrix)):
            for j in range (len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    mult[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(self.rows, self.columns, mult)

    def transpose(self):
        result = Matrix(self.columns, self.rows, [[0] * self.rows for _ in range(self.columns)])
        for i in range(self.rows):
            for j in range(self.columns):
                result.matrix[j][i] = self.matrix[i][j]
        return result

data1 = [[1, 2, 3], [4, 5, 6]]
m1 = Matrix(2, 3, data1)

data2 = [[7, 8, 9], [10, 11, 12]]
m2 = Matrix(2, 3, data2)

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1 + m2)

print("Вычитание матриц:")
print(m1 - m2)

data3 = [[1, 2], [3, 4], [5, 6]]
m3 = Matrix(3, 2, data3)

print("Умножение матриц:")
print(m1 * m3)

print("Транспонирование матрицы 1:")
print(m1.transpose())