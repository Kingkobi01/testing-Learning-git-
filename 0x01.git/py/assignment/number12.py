def remove_first_occurence(string, substring):
    
    new_string = string.replace(substring, "", 1)

    return new_string



print(remove_first_occurence("bicycle", "cyc"))