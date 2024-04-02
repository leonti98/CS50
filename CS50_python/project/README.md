# Financial Ledger Application
#### Video Demo: https://youtu.be/V9IXsEEzOo8

## Description
The Financial Ledger Application is a Python program designed to empower users in managing their finances effectively. It provides a comprehensive set of features to record expenses, incomes, and track the overall financial balance. The application ensures a user-friendly experience while offering insightful views into spending patterns and income sources.

## Features

### Record Expense
Users can record detailed expenses by providing a description, amount, and category. The program includes validation checks to ensure that the expense amount is a positive number. This feature is particularly useful for users to keep a detailed record of where their money is going.

### Record Income
The application allows users to record various sources of income, capturing the source name and the corresponding amount. Similar to expenses, the program validates that the income amount is a positive number. This feature aids users in understanding their diverse income streams.

### View Expenses
Users have the flexibility to view their expenses in two ways:
- **Overall Spendings:** Provides a summary of total spendings across all expense categories.
- **Category-specific Spendings:** Allows users to drill down into specific expense categories and view detailed spendings. This feature is beneficial for budgeting and identifying areas for potential savings.

### View Incomes
This feature enables users to view their total income from different sources. It provides a clear picture of the income distribution, aiding users in making informed financial decisions.

### View Balance
Users can check their current financial balance at any time. The balance reflects the net effect of recorded expenses and incomes, offering a real-time snapshot of the user's financial position.

### Exit
The application provides a simple exit option for users to gracefully end their session after managing their financial transactions.

## How to Use
1. Run the program.
2. Enter the starting balance.
3. Choose an action by entering a number from 1 to 6.

## Example Usage
1. Record a detailed expense, such as a monthly utility bill.
2. Record income from various sources, such as salary and freelance work.
3. View overall spendings to understand total expenses.
4. Drill down into specific expense categories, like 'Groceries,' for more detailed insights.
5. View total incomes to understand the distribution of income sources.
6. Check the current financial balance.
7. Exit the program.

## Files
- `financial_ledger.py`: Contains the main implementation of the FinancialLedger class and the main program loop.
- `test_project.py`: Contains tests for the FinancialLedger class.
- `README.md`: Documentation file explaining the project and its features.
- `requirements.txt`: Contains required libraries for this project.

## Design Choices
### Validation Checks
Validation checks for positive numerical amounts ensure data integrity and prevent accidental entry of negative amounts.

### User-Friendly Interface
The program features a simple and intuitive interface to cater to users with varying levels of technical expertise.

### Categorization
Categorizing expenses allows users to gain insights into their spending patterns, facilitating better financial planning.

### Modular Code
The code is designed with modularity in mind, making it easy for developers to extend or modify the application in the future.

## Error Handling
The Financial Ledger Application incorporates error handling mechanisms to enhance user experience and prevent unintended issues.

### Starting Balance Input
When entering the starting balance, the program expects a numerical input. If a non-numerical value is provided, a `ValueError` will be raised, prompting the user to enter a valid numerical starting balance.

### Expense and Income Amount Input
When recording expenses or incomes, the program validates that the entered amount is a positive number. If a non-numerical value or a negative amount is provided, a `ValueError` will be raised, guiding the user to enter a valid positive numerical amount.

### Viewing Expenses and Incomes
When attempting to view expenses or incomes, the program checks whether any transactions have been recorded. If there are no recorded expenses or incomes, the program informs the user accordingly, preventing potential confusion.

### Invalid Action Selection
The program prompts the user to choose an action by entering a number from 1 to 6. If an invalid input is provided, the program notifies the user and requests a valid input.

## Testing
The Financial Ledger Application includes a set of automated tests to ensure the correctness of its functionalities. The tests are implemented using the `pytest` framework and cover various aspects of the FinancialLedger class.

### Test File: `test_project.py`

#### Test Cases
1. **Initial Balance Test**: Checks if the initial balance is correctly set when creating a FinancialLedger instance.
2. **Expense Record Test**: Verifies the accuracy of expense recording and the resulting balance.
3. **Income Record Test**: Validates the correctness of income recording and the resulting balance.
4. **Category Spending Test**: Ensures that the category spending function returns the correct amounts and handles cases where no spendings are present for a category.
5. **Income Source Test**: Verifies the accuracy of the income source function and handles cases where no income is present for a specific source.
6. **Get Spendings Test**: Checks if the get_spendings function returns the expected dictionary of spending categories and amounts.
7. **Get Incomes Test**: Validates the correctness of the get_incomes function, ensuring it returns the expected dictionary of income sources and amounts.
8. **Balance After Transactions Test**: Confirms that the overall balance is calculated accurately after a sequence of transactions.

#### How to Run Tests
To run the tests, execute the following command in the terminal:

```bash
pytest test_project.py
