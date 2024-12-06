def several_zeros():
    liste=[0,0,0,0,0,0,0,0,0,0]
    return liste

def several_zeros_custom(nb_zeros=10):
    liste=[]
    for i in range(nb_zeros):
        liste.append(0)
    return liste

def matrix(rows, cols): 
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(0)
    return matrix

class Matrix:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._matrix[row][col]
        else:
            raise IndexError("les valeurs ne sont pas comprises dans la matrice")

    def __eq__(self, other):
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for i in range(self._rows):
            for j in range(self._cols):
                if self._matrix[i][j] != other._matrix[i][j]:
                    return False
        return True
    


def my_sort(my_list: [int]) -> [int]:
    sorted_list = my_list[:]
    n = len(sorted_list)
    for i in range(n):
        for j in range(n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j+1]
                sorted_list[j+1] = temp
    return sorted_list
    

        

        