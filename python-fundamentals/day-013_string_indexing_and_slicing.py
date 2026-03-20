
#//-------------------------------------------------------------------
#// #Day 13 - String Indexing & Slicing
#//-------------------------------------------------------------------

# @TASK: Complete the following exercises. You can check them as you go by
# running: python 023_string_indexing.py

# == Exercise One ==

print("")
print("Function: get_first_letter")

def get_first_letter(the_str):
  # Return the first letter of the string
 return (the_str[0])

check_that_these_are_equal(
  get_first_letter("The king granted them"),
  "T"
)

check_that_these_are_equal(
  get_first_letter("Five years later"),
  "F"
)

# == Exercise Two ==

print("")
print("Function: get_last_letter")

def get_last_letter(the_str):
  # Return the last letter of the string
  return (the_str[-1])

check_that_these_are_equal(
  get_last_letter("The king granted them"),
  "m"
)

check_that_these_are_equal(
  get_last_letter("Five years later"),
  "r"
)

# == Exercise Three ==

print("")
print("Function: get_nth_letter")

def get_nth_letter(the_str, n):
  # Return the letter of the string at the specified index
  return (the_str[n])

check_that_these_are_equal(
  get_nth_letter("The king granted them", 4),
  "k"
)

check_that_these_are_equal(
  get_nth_letter("Five years later", 7),
  "a"
)

# == Exercise Four ==

print("")
print("Function: get_letters_between_four_and_eight")

def get_letters_between_four_and_eight(the_str):
  # Return the section of the string between indexes four and eight
  return (the_str[4:8])

check_that_these_are_equal(
  get_letters_between_four_and_eight("The king granted them"),
  "king"
)

check_that_these_are_equal(
  get_letters_between_four_and_eight("Five years later"),
  " yea"
)