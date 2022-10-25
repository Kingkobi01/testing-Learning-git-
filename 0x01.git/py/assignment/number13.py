def remove_all(string, substring):
    new_string = string.replace(substring, "")
    return new_string


print(remove_all("bicycle", "eggs"))