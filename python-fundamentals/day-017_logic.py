from test_checks import check_that_these_are_equal
#//-------------------------------------------------------------------
#// #Day 17 - Logic
#//-------------------------------------------------------------------

# == Exercise One ==

print("")
print("Function: a_and_b")

def a_and_b(a, b):
  return a and b
  pass

check_that_these_are_equal(a_and_b(True, True), True)
check_that_these_are_equal(a_and_b(True, False), False)
check_that_these_are_equal(a_and_b(False, True), False)
check_that_these_are_equal(a_and_b(False, False), False)

# == Exercise Two ==

print("")
print("Function: not_a")

# Note that this operator only takes one value. The operator goes first, and the
# value second.
def not_a(a):
  return not(a)
  pass

check_that_these_are_equal(not_a(True), False)
check_that_these_are_equal(not_a(False), True)