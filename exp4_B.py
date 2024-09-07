def find_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

arr = [2, 3, 4, 5]
n = 7
remainder = find_remainder(arr, n)
print("Remainder of array multiplication divided by", n, ":", remainder)