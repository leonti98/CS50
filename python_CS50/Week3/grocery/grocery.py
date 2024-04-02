def grocery():
    groceries = {}
    while True:
        try:
            Item = input("")
            if Item not in groceries.keys():
                groceries[Item] = 1
            elif Item in groceries.keys():
                groceries[Item] = groceries[Item] + 1
        except EOFError:
            sorted_dict = dict(sorted(groceries.items()))
            for k, v in sorted_dict.items():
                print (v, k.upper())
            break


grocery()
