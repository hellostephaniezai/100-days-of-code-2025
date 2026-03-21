from test_checks import check_that_these_are_equal
#//-------------------------------------------------------------------
#// #Day 16 - Comparisons
#//-------------------------------------------------------------------

def check_that_these_are_equal(actual, expected):
    if actual == expected:
        print(f"✅ Passed: got {actual}")
    else:
        print(f"❌ Failed: got {actual}, expected {expected}")

# == Exercise One ==

print("")
print("Function: a_is_less_than_b")

def a_is_less_than_b(a, b):
  # Uncomment this next line and replace ?? with the right operator
  return a < b
  pass

check_that_these_are_equal(
  a_is_less_than_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_less_than_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_less_than_b(2, 1),
  False
)

# == Exercise Two ==

print("")
print("Function: a_is_greater_than_b")

def a_is_greater_than_b(a, b):
  return a > b
  pass

check_that_these_are_equal(
  a_is_greater_than_b(1, 2),
  False
)

check_that_these_are_equal(
  a_is_greater_than_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_greater_than_b(2, 1),
  True
)

# == Exercise Three ==

print("")
print("Function: a_is_less_than_or_equal_to_b")

def a_is_less_than_or_equal_to_b(a, b):
  return a <= b
  pass

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(2, 1),
  False
)

# == Exercise Four ==

print("")
print("Function: a_is_greater_than_or_equal_to_b")

def a_is_greater_than_or_equal_to_b(a, b):
  return a >= b
  pass

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(1, 2),
  False
)

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(2, 1),
  True
)

# == Exercise Five ==

print("")
print("Function: a_is_not_equal_to_b")

def a_is_not_equal_to_b(a, b):
  return a != b
  pass

check_that_these_are_equal(
  a_is_not_equal_to_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_not_equal_to_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_not_equal_to_b(2, 1),
  True
)

# == Exercise Six ==

print("")
print("Function: a_is_within_b")

# search for "python check if string contains
# substring"
def a_is_within_b(a, b):
  return a in b
  pass

check_that_these_are_equal(
  a_is_within_b("e", "hello"),
  True
)

check_that_these_are_equal(
  a_is_within_b("f", "hello"),
  False
)
