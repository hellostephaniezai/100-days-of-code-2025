from test_checks import check_that_these_are_equal
#-------------------------------------------------------------------
# Day 18 - List Indexing
#-------------------------------------------------------------------

# == Exercise One ==

print("")
print("Function: get_first_item")

def get_first_item(the_list):
  # Return the first item of the list
  return the_list[0]
  pass

check_that_these_are_equal(
  get_first_item(["a", "b", "c", "d", "e"]),
  "a"
)

check_that_these_are_equal(
  get_first_item([34, 44, 54, 64]),
  34
)

# == Exercise Two ==

print("")
print("Function: get_last_item")

def get_last_item(the_list):
  # Return the last item of the list
  return the_list[-1]
  pass

check_that_these_are_equal(
  get_last_item(["a", "b", "c", "d", "e"]),
  "e"
)

check_that_these_are_equal(
  get_last_item([34, 44, 54, 64]),
  64
)

# == Exercise Three ==

print("")
print("Function: get_nth_item")

def get_nth_item(the_list, n):
  # Return the item of the list at the specified index
  return the_list[n]
  pass

check_that_these_are_equal(
  get_nth_item(["a", "b", "c", "d", "e"], 3),
  "d"
)

check_that_these_are_equal(
  get_nth_item([34, 44, 54, 64], 1),
  44
)

# == Exercise Four ==

print("")
print("Function: get_items_between_one_and_three")

def get_items_between_one_and_three(the_list):
  # Return the section of the list between indexes one and three
  return the_list[1:3]
  pass

check_that_these_are_equal(
  get_items_between_one_and_three(["a", "b", "c", "d", "e"]),
  ["b", "c"]
)

check_that_these_are_equal(
  get_items_between_one_and_three([34, 44, 54, 64]),
  [44, 54]
)