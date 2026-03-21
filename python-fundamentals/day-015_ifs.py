#//-------------------------------------------------------------------
#// #Day 15 - If and Else Statement
#//-------------------------------------------------------------------

# @TASK: Complete these exercises

# == Exercise One ==

print("")
print("Function: is_first_of_the_month")

def is_first_of_the_month(day_number):
  # Return "First of the month!" if the day number is 1.
  # Return "Not first of the month" otherwise.
  if day_number == 1:
    return ("First of the month!")
  else:
    return ("Not first of the month")
  pass

check_that_these_are_equal(
  is_first_of_the_month(1),
  "First of the month!"
)

check_that_these_are_equal(
  is_first_of_the_month(12),
  "Not first of the month"
)

# == Exercise Two ==

print("")
print("Function: has_five_chars")

def has_five_chars(the_str):
  # Return "STRING is five characters long" if the string is five characters
  # long.
  # Otherwise, return "Not five characters".
  if len(the_str) == 5:
   return f"{the_str} is five characters long"
  else:
    return ("Not five characters")
  pass

check_that_these_are_equal(
  has_five_chars("ABCDE"),
  "ABCDE is five characters long"
)

check_that_these_are_equal(
  has_five_chars("FORGE"),
  "FORGE is five characters long"
)

check_that_these_are_equal(
  has_five_chars("Nope"),
  "Not five characters"
)

check_that_these_are_equal(
  has_five_chars("Nor this one"),
  "Not five characters"
)
