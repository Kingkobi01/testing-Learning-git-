""" Write a function num_even_digits(n) that counts the number of even digits in n. These tests should pass: """

def num_even_digits(number):
    number_str = str(number)
    number_of_even_numbers = 0
    for letter in number_str:
        if int(letter) % 2 == 0:
            number_of_even_numbers += 1
    
    return number_of_even_numbers



print(num_even_digits(123456789)) # SHould return  4
