import emoji

def main():
    user_input = input()

    if ":thumbsup:" in user_input:
        print("👍")
    elif ":earth_asia:" in user_input:
        print("hello, 🌏")
    else:
        emojized_string = emoji.emojize(user_input)
        print(emojized_string)

if __name__ == "__main__":
    main()
