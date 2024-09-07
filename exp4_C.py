def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, d):
    n = len(arr)
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n-1)
    reverse_array(arr, 0, n-1)

arr = [1, 2, 3, 4, 5]
print("Original array: ", arr)
d = 2

rotate_array(arr, d)
print("Rotated array: ", arr)