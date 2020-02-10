"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("x is %2d" %(x))
print("y is %4.2f" %(y))
print('z is "%2s"' %(z))


# Use the 'format' string method to print the same thing

print("x is {0}".format(x))
print("y is {0:4.2f}".format(y))
print('z is "{0}"'.format(z))

# Finally, print the same thing using an f-string
print(f"x is {x}")
print(f"y is {y:.2f}")
print(f'z is "{z}"')