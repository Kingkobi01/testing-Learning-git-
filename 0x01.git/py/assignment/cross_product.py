def cross_product(u, v):
    if len(u) and len(v) != 3:
        print("The two vectors should have only 3 values!")
        return
    else:
        product = [
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0],
        ]
    return product



