from project import main, FinancialLedger


def test_initial_balance():
    ledger = FinancialLedger(balance=1000)
    assert ledger.get_balance() == 1000


def test_expense_record():
    ledger = FinancialLedger(balance=1000)
    ledger.expense("Groceries", 50, "Food")
    assert ledger.get_balance() == 950
    assert ledger.category_spending("Food") == 50


def test_income_record():
    ledger = FinancialLedger(balance=1000)
    ledger.income("Salary", 2000)
    assert ledger.get_balance() == 3000
    assert ledger.income_source("Salary") == 2000


def test_category_spending():
    ledger = FinancialLedger(balance=1000)
    ledger.expense("Groceries", 50, "Food")
    ledger.expense("Movie", 20, "Entertainment")
    assert ledger.category_spending("Food") == 50
    assert ledger.category_spending("Entertainment") == 20
    assert ledger.category_spending("Clothing") == "no spendings on Clothing"


def test_income_source():
    ledger = FinancialLedger(balance=1000)
    ledger.income("Salary", 2000)
    ledger.income("Freelance", 500)
    assert ledger.income_source("Salary") == 2000
    assert ledger.income_source("Freelance") == 500
    assert ledger.income_source("Investments") == "no income from Investments"


def test_get_spendings():
    ledger = FinancialLedger(balance=1000)
    ledger.expense("Groceries", 50, "Food")
    ledger.expense("Movie", 20, "Entertainment")
    ledger.expense("Clothes", 30, "Clothing")
    spendings = ledger.get_spendings()
    assert spendings == {"Food": 50, "Entertainment": 20, "Clothing": 30}


def test_get_incomes():
    ledger = FinancialLedger(balance=1000)
    ledger.income("Salary", 2000)
    ledger.income("Freelance", 500)
    incomes = ledger.get_incomes()
    assert incomes == {"Salary": 2000, "Freelance": 500}


def test_balance_after_transactions():
    ledger = FinancialLedger(balance=1000)
    ledger.expense("Groceries", 50, "Food")
    ledger.income("Salary", 2000)
    ledger.expense("Movie", 20, "Entertainment")
    assert ledger.get_balance() == 2930
