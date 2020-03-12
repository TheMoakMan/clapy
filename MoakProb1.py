
from errors import *

class Matrix():
    
    def __init__(self, row, col, matrix=[]):
        self.shape=(row,col)
        self.arr = matrix

        print(row, col, matrix)

        if row != len(matrix):
            raise DimError
    
        for n in range(row):
         
            if type(matrix[n]) != list or len(matrix[n]) != col:
                raise DimError


        # Default to matrix of all 0's
        if self.arr == []:
            for i in range(self.shape[0]):
                self.arr += [[0]]
                for _ in range(self.shape[1] - 1):
                    self.arr[i] += [0]

        





        





    

