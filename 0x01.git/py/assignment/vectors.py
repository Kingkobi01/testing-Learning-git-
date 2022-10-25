def add_vector(u, v):
    sum_vector = []
    if len(u) != len(v):
        raise Exception("The two Vectors Should be of the same length!!")
    else:
        for i in range(len(u)):
            sum = u[i] + v[i]
            sum_vector.append(sum)
    return sum_vector


# print(add_vector([1, 2], [1, 4]) == [2, 6])


def scalar_multiply(s, v):
    scaled_vector = []
    for i in v:

        scaled_vector.append(i * s)

    return scaled_vector


print(scalar_multiply(3, [1, 0, -1]) == [3, 0, -3
])
