import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class AccountingProgram:
    def __init__(self, root):
        """
        Intialize accounting program

        paramters:
        root - root window for tinker
        """
        self.transactions = []
        self.root = root
        self.root.title("Accounting Program")
        self.lable = tk.Label(root, text="Accounting program")

        #buttons

    def record_transaction(self):
            #record transaction (income/expense)
            ...

    def submit_transaction(self):
        """
            transaction = {
                "Description" = description,
                "Amount" = amount,
                "Type" = transaction_type
            }
        """
        ...

    def get_reports_and_taxes(self):
        ...


def main():
    root = tk.Tk()
    app = AccountingProgram(root)
    root.mainloop()

if __name__ == "__main__":
    main()
