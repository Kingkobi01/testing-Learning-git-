
def substring_counter(string, substring):

    
    result = [i for i in range(len(string)) if string.startswith(substring, i)]

    return len(result)



print(substring_counter("aaaaaa", "aaa"))


