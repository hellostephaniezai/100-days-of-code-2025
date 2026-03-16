#//-------------------------------------------------------------------
#// #Day 10 - Function Add numbers
#//-------------------------------------------------------------------

# @TASK 1 : Write a function called `add_numbers` that:
#
# * Takes two numbers as input
# * Adds them together
# * Returns the result

# YOUR FUNCTION GOES BELOW THIS LINE

def add_numbers(num_a,num_b):
  return num_a + num_b

print("add_numbers(2, 3) is:")

# TASK 2 : Arithmetic Operators

# Section 1 - Examples 

# # Addition
added = 2 + 3
print(f"2 + 3 = {added} (should be 5)")

# Multiplication
multiplied = 2 * 3
print(f"2 * 3 = {multiplied} (should be 6)") 

#--------------------------------------------------------------

# Section 2 - Researched and Actioned Task

# == Subtraction ==

subtracted = 2 - 3
print(f"2 - 3 = {subtracted} (should be -1)")

# == Division ==

divided = 2 / 3
print(f"2 / 3 = {divided} (should be 0.6666666666666666)")

# This kind of 'decimal point' number, 0.6666666666666666 is called a float, by
# the way, meaning 'floating point'.

# == Modulus == Sometimes known as "remainder if we divide 3 by 2"

modulus = 3 % 2
print(f"3 ? 2 = {modulus} (should be 1)")

# == Floor division == Sometimes known as "division without remainder"

floor_divided = 2 // 3
print(f"2 // 3 = {floor_divided} (should be 0)")

# == Exponentiation == Sometimes known as "2 to the power of 3"

expr = 2 ** 3
print(f"2 ** 3 = {expr} (should be 8)")

# There are many more operators in Python that you can research. You're very
# welcome to try out a few below:

# OPERATOR PLAYGROUND STARTS

x = 10 
x += 3

y = 15
y -= 5

k = 20
k **= 2

b = 20
b *= 4

print(x)
print(y)
print(k)
print(b)

# OPERATOR PLAYGROUND ENDS