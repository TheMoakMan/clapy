
from errors import *

class Matrix():
    
    def __init__(self, row, col, matrix=[]):
        self.shape=(row,col)
        self.arr = matrix

        print(row, col, matrix)

        # Check if matrix dim are equal to specified dimensions
        if row != len(matrix):
            raise DimError(DIM_ERR)
    
        for n in range(row):
         
            if type(matrix[n]) != list or len(matrix[n]) != col:
                raise DimError(DIM_ERR)

        # Default to matrix of all 0's
        if self.arr == []:
            for i in range(self.shape[0]):
                self.arr += [[0]]
                for _ in range(self.shape[1] - 1):
                    self.arr[i] += [0]

    # Adjusting matrix

    # Length of Vector

    # Transpose of Matrix
    
    # Conjugate of Matrix
    
    # Adjoint of Matrix
    
    # Matrix Multiplication
    
    # Scalar Multiplication (int or float) * matrix  

    # Print out entire matrix
    # def show(self)

    # bracket operators? so you don't have to call .arr for []

    # Basis

    # Inner Product of Matrices

    # Kroneker Product










        

        





        





    

