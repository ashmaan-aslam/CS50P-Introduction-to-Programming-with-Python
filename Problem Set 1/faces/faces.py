def main():
    a = input()
    print(convert(a))

def convert(x):
    x = str(x)
    happy = "🙂"
    sad = "🙁"
    x = x.replace(":)", happy )
    x = x.replace(":(", sad)
    return x

main()
