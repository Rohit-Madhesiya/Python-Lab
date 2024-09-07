row = int(input("Enter Row:"))
col = int(input("Enter column:"))
mat = [[0]*col]*row
for i in range(row):
  for j in range(col):
    mat[i][j] = int(input())

print("Original Matrix:")
for i in range(row):
  for j in range(col):
    print(mat[i][j], end=" ")
  print()
  
def trans(A, B, row, col):
  for i in range(row):
    for j in range(col):
      B[i][j] = A[j][i]
  return B

transpose = mat[:][:]
transpose = trans(mat, transpose, row, col)

print("Original Matrix:")
for i in range(row):
  for j in range(col):
    print(mat[i][j], end=" ")
  print()

print("Transpose Matrix:")
for i in range(row):
  for j in range(col):
    print(transpose[i][j], end=" ")
  print()


