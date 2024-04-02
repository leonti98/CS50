from tabulate import tabulate


class FinancialLedger:
    def __init__(self, balance):
        self._expenses = []
        self._incomes = []
        self._balance = balance

    def expense(self, description, amount, category):
        """
        record expense transaction:

        :param decription: descrioption what money was spent on
        :type description: str

        :param amount: amount spent on transaction.
        :type description: float
        :raise: ValueError: if given amount is negative.

        :param category: category indicating the purpose of the expense.
        :type category: str
        """
        amount = float(amount)
        if amount < 0:
            raise ValueError("expense amount should be positive number")
        expense = {
            "description": description,
            "amount": amount,
            "category": category,
        }
        self._expenses.append(expense)
        self._balance -= amount

    def income(self, source, amount):
        """
        Record an income transaction.

        :param source: The source or origin of the income.
        :type source: str

        :param amount: The amount of income received.
        :type amount: int or float
        :raise ValueError: If the given amount is negative.
        """
        amount = float(amount)
        if amount < 0:
            raise ValueError("income amount should be positive number")
        expense = {
            "source": source,
            "amount": amount,
        }
        self._incomes.append(expense)
        self._balance += amount

    def category_spending(self, category):
        """
        Return the total expenses for a given category.

        :param category: category for which expenses are to be calculated.
        :type category: str
        :return: The total amount spent in the specified category.
                If no expenses are found, return a string indicating no spendings.
        :rtype: float or str
        """
        category_balance = 0
        for expense in self._expenses:
            if category == expense["category"]:
                category_balance += expense["amount"]
        if category_balance > 0:
            return category_balance
        else:
            return f"no spendings on {category}"

    def income_source(self, source):
        """
        Return the total income from a given source.

        :param source: The source from which the income is received.
        :type source: str
        :return: The total amount of income received from the specified source.
                If no income is found, return a string indicating no income.
        :rtype: float or str
        """
        income_balance = 0
        for income in self._incomes:
            if source == income["source"]:
                income_balance += income["amount"]
        if income_balance > 0:
            return income_balance
        else:
            return f"no income from {source}"

    def get_spendings(self):
        """
        Get the total spending for each spending category.

        :return: A dictionary where keys are spending categories and values are the total
                amount spent in each category.
        :rtype: dict
        """
        categories = []
        all_spendings = {}
        # Loop through each expense and add unique spending categories to the categories list
        for expense in self._expenses:
            if expense["category"] not in categories:
                categories.append(expense["category"])
        # add category to all_spendings dictionary
        for category in categories:
            if category not in all_spendings:
                # add to dictionary, where key = category name and value = all spendings in that category
                all_spendings[category] = self.category_spending(category)

        return all_spendings

    def get_incomes(self):
        """
        Get the total income for each income source.

        :return: A dictionary where keys are income sources and values are the total
                amount of income received from each source.
        :rtype: dict
        """
        sources = []
        all_incomes = {}
        # Loop through each income and add unique income sources to the sources list
        for income in self._incomes:
            if income["source"] not in sources:
                sources.append(income["source"])
        # add source to all_incomes dictionary
        for source in sources:
            if source not in all_incomes:
                # add to dictionary, key source name and value of all incomes in within that source
                all_incomes[source] = self.income_source(source)

        return all_incomes

    def get_balance(self):
        return self._balance

    def __str__(self):
        money_left = self.get_balance()
        return f"Balance = ${money_left}"


def main():
    try:
        starting_balance = float(input("Enter starting balance: $"))
    except:
        raise ValueError("Balance should be numerical")
    ledger = FinancialLedger(balance=starting_balance)

    while True:
        print(
            "\nSelect action \n1. Record Expense\n2. Record Income\n3. View Expenses\n4. View incomes\n5. View Balance\n6. Exit\n"
        )
        # make user choose action
        choice = input("Select action(1-6): ")

        if choice == "1":
            print("\nRecord Expense")
            description = input("Enter Expense Description: ")

            try:
                amount = float(input("Enter Amount: $"))
            except:
                print("\nAmount should be numerical!!!")
                continue

            category = input("Enter Expense Category: ")
            ledger.expense(description, amount, category)
            print(f"\nExpense of ${amount} for {category} recorded")
            print(ledger)

        elif choice == "2":
            print("\nRecord Income")
            source = input("Enter source: ")
            try:
                amount = float(input("Enter Amount: $"))
            except:
                print("\nAmount should be numerical!!!")
                continue
            ledger.income(source, amount)
            print(f"\nIncome of ${amount} from {source} recorded")
            print(ledger)

        elif choice == "3":
            if ledger._expenses:
                in_choice = input(
                    "\nSelect action \n1.View spendings by categoty\n2.View spendings on selected category\nAction(1-2): "
                )
                if in_choice == "1":
                    expenses = ledger.get_spendings()
                    headers = ["category", "amount in $"]
                    print(tabulate(expenses.items(), headers=headers, tablefmt="grid"))

                elif in_choice == "2":
                    category = input("Input category: ")
                    filtered_expenses = [
                        {"description": item["description"], "amount": item["amount"]}
                        for item in ledger._expenses
                        if item.get("category") == category
                    ]
                    headers = ["description", "amount in $"]
                    if filtered_expenses:
                        expenses_dict = {
                            item["description"]: item["amount"]
                            for item in filtered_expenses
                        }
                        print(
                            tabulate(
                                expenses_dict.items(), headers=headers, tablefmt="grid"
                            )
                        )
                    else:
                        print("\nInput existing category")
                else:
                    print("Input 1 or 2 when viewing expenses")
            else:
                print("\nyou have not recorded expenses")

        elif choice == "4":
            if ledger._incomes:
                incomes = ledger.get_incomes()
                headers = ["source", "amount in $"]
                print(tabulate(incomes.items(), headers=headers, tablefmt="grid"))

            else:
                print("\nyou have not recorded incomes")

        elif choice == "5":
            print(f"\n{ledger}")

        elif choice == "6":
            break

        else:
            print("CHOOSE NUMBER FORM 1 TO 6")


if __name__ == "__main__":
    main()
