import validators

email = input("Email: ").lower()
if validators.email(email):
    print("Valid")
else:
    print("Invalid")
