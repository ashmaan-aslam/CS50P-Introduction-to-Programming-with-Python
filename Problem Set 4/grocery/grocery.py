user_items = {}

while True:
    try:
        item = input().strip().lower()

        if item in user_items:
            user_items[item] += 1
        else:
            user_items[item] = 1

    except EOFError:
        break


sorted_dict = dict(sorted(user_items.items()))


for item in sorted_dict:
    print(sorted_dict[item], item.upper())
