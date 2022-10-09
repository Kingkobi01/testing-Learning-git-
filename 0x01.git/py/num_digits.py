""" What will num_digits(0) return? Modify it to return 1 for this case. Why does a call to num_digits(-24) result in an infinite loop? (hint: -1//10 evaluates to -1) Modify num_digits so that it works correctly with any integer value. Add these tests:

 """


def num_digits(number):
    stringified_number = str(number)
    return len(stringified_number)

print(num_digits(12345)) # Should return 5

print(num_digits(0))  # Should return 1 