import json

class BudgetTracker:
    def _init_(self):
        self.transactions = []  # Initialize transactions list in _init_

    def add_transaction(self, category, amount, transaction_type):
        self.transactions.append({"category": category, "amount": amount, "type": transaction_type})

    def calculate_budget(self, ):
        total_expenses = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "expense")
        total_income = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "income")
        remaining_budget =  total_income - total_expenses
        return remaining_budget

    def analyze_expenses(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction["type"] == "expense":
                category = transaction["category"]
                amount = transaction["amount"]
                if category in expense_categories:
                    expense_categories[category] += amount
                else:
                    expense_categories[category] = amount
        return expense_categories

    def save_transactions(self, filename):
        with open(filename, "w") as file:
            json.dump(self.transactions, file)

    def load_transactions(self, filename):
        with open(filename, "r") as file:
            self.transactions = json.load(file)

def main():
    tracker = BudgetTracker()

    # Load previous transactions if available
    filename = "transactions.json"
    try:
        tracker.load_transactions(filename)
        print("Previous transactions loaded successfully.")
    except FileNotFoundError:
        print("No previous transactions found.")

    # Main menu
    while True:
        print("\nBudget Tracker")
        print("1. Add Transaction")
        print("2. Calculate Remaining Budget")
        print("3. Analyze Expenses")
        print("4. Save Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (expense/income): ")
            if category.lower() in ["expense", "income"]:
                amount = float(input("Enter amount: "))
                transaction_type = category.lower()
                tracker.add_transaction(category, amount, transaction_type)
                print("Transaction added successfully.")
            else:
                print("Invalid category. Please enter 'expense' or 'income'.")

        elif choice == "2":
            remaining_budget = tracker.calculate_budget()
            print(f"Remaining budget: {remaining_budget}")

        elif choice == "3":
            expense_categories = tracker.analyze_expenses()
            print("Expense Analysis:")
            for category, amount in expense_categories.items():
                print(f"{category}: {amount}")

        elif choice == "4":
            tracker.save_transactions(filename)
            print("Transactions saved successfully.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

main()