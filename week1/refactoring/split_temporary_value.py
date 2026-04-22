height = 5
width = 10
# You have a local variable that’s used to store various intermediate values inside a method (except for cycle variables).
temp = 2 * (height + width)
print(temp)
temp = height * width
print(temp)

# Use different variables for different values. Each variable should be responsible for only one particular thing.

perimeter = 2 * (height + width)
print(perimeter)
area = height * width
print(area)