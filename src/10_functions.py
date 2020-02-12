# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(a):
    if (a % 2) == 0:
        return True
    else:
        return False


print(is_even(1))  # if number is even => true else: false

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print("even" if (num % 2) == 0 else "odd")
