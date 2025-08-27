z = {"Alice":63, "Ansh":100, "Mayank":0, "Priyanshu":80}

x = input("Enter your name: ").capitalize()

y=z.get(x)

if y is not None:
    print("{}'s marks : {}".format(x, y))
else:
    print("Student not found")
