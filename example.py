def matmult(m1, m2):
    tmp, result_matrix = []
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums=0
            for k in range(len(m2)):
                sums=sums+(m1[i][k]*m2[k][j])
            tmp.append(sums)
        result_matrix.append(tmp)
        tmp = []
    return result_matrix

def show_matrix(matrix):
    for row in matrix:
        print("|", end="\t")
        for el in row:
            print(round(el), end="\t")
        print("|\n")
            


A = [[1, 2], [3, 2]]
B = [[3, 2], [1, 1]]


C = [
  [2, 5],
  [6, 7],
  [1, 8],
]


D = [
  [1, 2, 1],
  [0, 1, 0],
]


    
print("Result: ")
show_matrix(matmult(A, B))