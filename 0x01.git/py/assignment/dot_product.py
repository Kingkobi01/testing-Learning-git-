

def dot_product(u, v):
    if len(u) != len(v):
        print("The two vectors should be of the same size!")
        return 
    else:
        sum = 0
        for i in range(len(u)):
            sum += (u[i] *v[i])


    return sum


print(dot_product([1,1], [1,1, 2]) == 2)