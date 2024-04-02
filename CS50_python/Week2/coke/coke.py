price = 50
print(f"Ammount Due: {price}")

while price >= 0:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        price = price - insert_coin
        if price > 0:
            print(f"Amount Due: {price}")
        else:
            print(f"Change Owed: {abs(price)}")
            break
    else:
        print(f"Amount Due: {price}")
