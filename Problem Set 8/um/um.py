import re
import sys
import string

# taking input
def main():
    print(count(input("Text: ")))


def count(s):
    text = s.split()
    count = 0

    # iterating over words in sentence to check if equal to "um"
    for word in text:
        cleanedword = word.strip(string.punctuation).lower()

        if cleanedword == "um":
            count += 1

    return count

if __name__ == "__main__":
    main()
