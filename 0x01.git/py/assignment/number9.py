def remove_letter(word, letter):
    new_word = ""
    for char in word:
        if char != letter:
            new_word += char

    return new_word


print(remove_letter("apple", "a"))  # Should print "pple"

print(remove_letter("Mississippi", "i"))
