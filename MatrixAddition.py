def add_matrices(matrix1, matrix2):
  result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
  return result_matrix

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
result_matrix = add_matrices(matrix1, matrix2)

print("Resultant matrix:")
for row in result_matrix:
  print(row)
