#//-------------------------------------------------------------------
#// #Test Checks 
#//

def check_that_these_are_equal(actual, expected):
    if actual == expected:
        print(f"✅ Passed: got {actual}")
    else:
        print(f"❌ Failed: got {actual}, expected {expected}")