from test_checks import check_that_these_are_equal
#//-------------------------------------------------------------------
#// #Day 12 - Two Step functions
#//-------------------------------------------------------------------

# @TASK: Complete these functions.

# == Exercise One ==

print("divide_by_two_and_add_one")
print("Function: divide_by_two_and_add_one")

def divide_by_two_and_add_one(num):
  #divide num by two and add one
  return (num / 2) + 1

check_that_these_are_equal(
  divide_by_two_and_add_one(6),
  4.0
)

# == Exercise Two ==

print("multiply_by_forty_and_add_sixty")
print("Function: multiply_by_forty_and_add_sixty")

def multiply_by_forty_and_add_sixty(num):
  # Multiply num by forty, and then add sixty
  return (num * 40 )+ 60

check_that_these_are_equal(
  multiply_by_forty_and_add_sixty(3423),
  136980
)

# == Exercise Three ==

print("add_together_and_double(num_a, num_b")
print("Function: add_together_and_double")

def add_together_and_double(num_a, num_b):
  # Add together num_a and num_b, then double the result
  return (num_a + num_b) * 2

check_that_these_are_equal(
  add_together_and_double(3, 4),
  14
)


#Completed the above functions 