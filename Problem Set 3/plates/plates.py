def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #All vanity plates must start with at least two letters.
    if not s[0:2].isalpha():
        return False

    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if not (2 <= len(s) <= 6):
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

            if s[i] == "0":
                return False
            break

    #No periods, spaces, or punctuation marks are allowed
    if not s.isalnum():
        return False

    return True

main()
