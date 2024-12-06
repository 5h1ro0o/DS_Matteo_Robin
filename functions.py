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

class Matrix : 
    def __init__(self):
        self.rows = 0
        self.cols = 0

    def create(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        for i in range(rows):
            self.matrix.append([])
            for j in range(cols):
                self.matrix[i].append(0)
        return self.matrix
    
    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix[row][col]
        else:
            raise IndexError("les valeurs ne sont pas comprises dans la matrice")
        
    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True
    


def sorting_list(my_list: [int]) -> [int]:
    sorted_list = my_list[:]
    n = len(sorted_list)
    for i in range(n):
        for j in range(n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j+1]
                sorted_list[j+1] = temp
    return sorted_list
    

        

        