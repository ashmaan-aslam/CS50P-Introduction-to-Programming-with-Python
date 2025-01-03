import inflect

p = inflect.engine()

names = []
try:
    while True:
        name = input("Input: ")
        names.append(name)
except EOFError:
    pass

correctnames = p.join(names)
print(f"Adieu, adieu, to {correctnames}")

