import random


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []
        
        for i in range(0, rows):
            self.data.append([])
            for j in range(0, cols):
                self.data[i].append(0)
        
    def multiply(self, n):
        if isinstance(n, Matrix):
            if self.rows != n.rows or self.cols != n.cols:
                raise ValueError("Matrices must have the same dimensions")
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= n.data[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= n

    @staticmethod
    def multiply_matrices(a, b):
        if a.cols != b.rows:
            print("Columns of A must match rows of B.")
            return None

        result = Matrix(a.rows, b.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                total = 0
                for k in range(a.cols):
                    total += a.data[i][k] * b.data[k][j]
                result.data[i][j] = total
        return result

    def add(self, n):
        if isinstance(n, Matrix):
            if self.rows != n.rows or self.cols != n.cols:
                raise ValueError("Matrices must have the same dimensions")
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n.data[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n

    def random(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.data[i][j]= random.randint(-1,1)
    @staticmethod
    def transpose(a):
        result = Matrix(a.cols, a.rows)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[j][i] = a.data[i][j]
        return result
                
    def map(self, fn):
        #Apply a function to every elemnt of the matrix
        for i in range(self.rows):
            for j in range(self.cols):
                value= self.data[i][j]
                self.data[i][j]= fn(value)
    
    @staticmethod
    def map_static(matrix, fn):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.data[i][j] = fn(matrix.data[i][j])
        return result
    @staticmethod
    def fromarray(array):
        m = Matrix(len(array), 1)
        for i in range(len(array)):
            m.data[i][0] = array[i]
        return m
    
    def toArray(self):
        array=[]
        for i in range(self.rows):
            for j in range(self.cols):
                array.append(self.data[i][j])
        return array
    @staticmethod
    def subtract(a,b):
        result=Matrix(a.rows,a.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j]= a.data[i][j]-b.data[i][j]
        return result
    def print(self):
        for i in range(self.rows):
            print(self.data[i])
        print()

