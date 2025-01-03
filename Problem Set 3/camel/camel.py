import re

camelCase = input(str("camelCase: "))

def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

print(camel_to_snake(camelCase))
