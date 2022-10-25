
def count_letters(fruit, letter):
    fruit = fruit
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    
    return count



print(count_letters("Dangote", "n")) # Should print 1

print(count_letters("Samuel", "i")) # Should print 0


