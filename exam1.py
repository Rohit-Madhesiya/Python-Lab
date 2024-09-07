mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# trans = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
# print("Original Matrix:")
# for i in mat:
#   print(i)
# print("Transpose Matrix:")
# for i in trans:
#   print(i)

# mat2=[[4,3,2],[7,6,5],[9,8,0]]
# if len(mat1[0]) != len(mat2):
#   print("Invalid Matrix Dimensions.")
# else:
#   mat3=[[0,0,0],[0,0,0],[0,0,0]]
#   for i in range(len(mat1)):
#     for j in range(len(mat2[0])):
#       for k in range(len(mat2)):
#         mat3[i][j]+=mat1[i][k]*mat2[k][j]
#   print("Matrix Result:")
#   for i in mat3:
#     print(i)

# def isPrime(num):
#   if num==1:
#     return False
#   elif num==2 or num==3 or num==5:
#     return True
#   elif num%2==0 or num%3==0:
#     return False
#   else:
#     for i in range(num,6):
#       if num%i==0:
#         return False
#       elif num%(i+2)==0:
#         return False
#     return True

# num=int(input("Enter number:"))
# print(num,"is prime:",isPrime(num))

# def fibonacii(num):
#   if num==0:
#     return 0
#   elif num==1:
#     return 1
#   else:
#     return fibonacii(num-1)+fibonacii(num-2)
# num=int(input("Enter number:"))
# print("Fibonacii of ",num,"is:",fibonacii(num))

# def factorial(num):
#   if num == 0 or num == 1:
#     return 1
#   else:
#     return num * factorial(num - 1)

# num = int(input("Enter Number:"))
# print("Factorial of num", num, "is: ", factorial(num))

# def isArmstrong(num):
#   res=0
#   temp=num
#   while temp>0:
#     res=res+(temp%10)**3
#     temp//=10
#   if res==num:
#     return True
#   return False

# num=int(input("Enter number:"))
# print("Armstrong is ",num,":",isArmstrong(num))

# for i in range(4):
#   for j in range(i + 1):
#     print("MMM", end=" ")
#   print("")

str = [
    "Hello", "mr.", "Anubhav", "Tiwari", "What", "are", "you", "doing",
    "right", "now"
]
str1 = sorted(str, key=len)
print(str1)
