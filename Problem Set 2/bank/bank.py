greeting = input("Greeting: ")
lower_greeting = greeting.lower()

if "hello" in lower_greeting:
    print("$0")
elif "what" in lower_greeting:
    print("$100")
elif "h" in lower_greeting:
    print("$20")
else:
    print("$100")
