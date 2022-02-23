def pyramid(x):
    y = x-1
    for s in range(0, x):
        for t in range(0, y):
            print(end=" ")
        y = y - 1
        for t in range(0, s + 1):
            print("* ", end="")
        print("")
x = 5
pyramid(x)

