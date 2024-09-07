for i in range(4):
  for j in range(i + 1):
    print("MMM", end=' ')
  print()

#print(1**2)
#print(4//2)


def fib(n):
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)


for i in range(int(input("Enter Range:"))):
  print(fib(i),end=' ')

# Enter Range: 5
# 0 1 1 2 3

print("Enter the row and column size of first matrix:")
r1=int(input())
c1=int(input())
mat1=[]

for i in range(r1):
  mat1[i]=[]
  for j in range(c1):
    mat1[i].append(int(input("Enter Element"+str(i)+str(j)+":")))
    
print("Enter the row and column size of second matrix:")
r2=int(input())
c2=int(input())
mat2=[]
for i in range(r2):
  mat2[i]=[]
  for j in range(c2):
    mat2[i].append(int(input("Enter Element"+str(i)+str(j)+":")))

if c1 != r2:
  print("Matrices cannot be multiplied")

res=[]
for i in range(r1):
  res.append([])
  for j in range(c2):
    res[i].append(0)
    for k in range(c1):
      res[i][j]+=mat1[i][k]*mat2[k][j]

print("Matrix Multiplication: ")
for i in range(r1):
  for j in range(c2):
    print(res[i][j],end=" ")
  print()
