a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

b = a.lower()
c = b.strip()

if c == "42":
    print("Yes")
elif c == "forty-two":
    print("Yes")
elif c == "forty two":
    print("Yes")
else:
    print("No")
