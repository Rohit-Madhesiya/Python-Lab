def is_perfect_square(n):
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n

def is_fibonacci_multiple(n, x):
    return is_perfect_square(5 * (x ** 2) + 4) or is_perfect_square(5 * (x ** 2) - 4)

n = int(input("Enter the value of n: "))
num = 0
count = 0

while count < n:
    if is_fibonacci_multiple(n, num):
        print(num)
        count += 1
    num += 1