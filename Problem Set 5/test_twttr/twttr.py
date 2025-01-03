def main():
    input1= input("Input: ")
    input1= str(input1)
    print(shorten(input1))

def shorten(word):
    new_text = ""
    for letter in word:
        if letter not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            new_text += letter
    return new_text

if __name__ == "__main__":
    main()
