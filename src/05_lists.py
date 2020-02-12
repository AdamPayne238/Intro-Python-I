# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)  # append() adds its arguments as a single element to the end of a list
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)  # extend() method takes a list as an argument and adds it to the end
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)  # pop() python function that removes and returns the last value from a list
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)  # insert(index, element) inserts an element at a given index, shifting elements to the right
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))  # len() prints the length of the value being passed into it

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in range(0, len(x)):  # for loop w/ range between 0 and length of x / prints index of i * 1000
    print(x[i] * 1000)
