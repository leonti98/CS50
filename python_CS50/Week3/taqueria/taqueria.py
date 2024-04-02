d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def price_calc():
    total_price = 0
    while True:
        try:
            item = (input("Item: ")).title()
            if item in d:
                price = float(d[item])
                total_price = total_price + price
                print (f"Total: ${("%.2f" % total_price)}")
        except EOFError:
            print ("")
            break

price_calc()
