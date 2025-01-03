amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    insert_coin = input("Insert Coin: ")

    try:
        insert_coin = int(insert_coin)
    except ValueError:
        continue

    if insert_coin in [25, 10, 5]:
        amount_due -= insert_coin
    else:
        continue

    if amount_due <= 0:
        change_owed = abs(amount_due)
        print(f"Change Owed: {change_owed}")
        break
