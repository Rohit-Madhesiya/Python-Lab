# Create a list
my_list = []

# Insert an element at a specific index
my_list.insert(0, 'apple')
my_list.insert(1, 'banana')
my_list.insert(2, 'cherry')
print(my_list)
# Remove an element from the list
my_list.remove('banana')
print(my_list)
# Append an element to the end of the list
my_list.append('orange')
print(my_list)
# Get the length of the list
list_length = len(my_list)
print(list_length)
# Remove and return the element at the specified index
popped_element = my_list.pop(0)
print(popped_element)
# Clear the entire list
my_list.clear()
print(my_list)
