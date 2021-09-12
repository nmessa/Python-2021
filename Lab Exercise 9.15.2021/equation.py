for x in range(1, 10):
    for y in range(1,10):
        for z in range(1, 10):
            if x + 3*y+5*x == x*y*z:
                print(x, y, z)
