from datetime import date

class Transaction:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"Date: {self.date}, Category: {self.category}, Amount: ${self.amount}, Description: {self.description}"

    def validate(self):
        categories = {"Housing", "Transportation", "Food", "Utilities", "Insurance", "Healthcare", "Savings & Investments", "Entertainment", "Misc"}
        while True:
            try:  
                #Validate date  
                self.date = input("Enter the date of transaction (yyyy-mm-dd): ")
                self.date = date.fromisoformat(self.date)   #Can also use the strptime method from the datetime module here
        
                #Validate category
                print("Available categories: "f"{", ".join(sorted(categories))}")
                self.category = input("Select a category from the set: ").title()
                if self.category not in categories:
                    raise ValueError("This is not a valid category!")
                print("This category exists.")
        
                #Validate amount
                self.amount = float(input("Enter the amount: $"))
                if self.amount <=0:
                    raise ValueError("Amount must be greater than zero!")

                #Validate description
                self.description = input("Enter a description: ")
                if 6 <= len(self.description) <= 255:
                    pass
                else:
                    raise ValueError("Description should have atleast 6 characters!")
            
                break
            except ValueError as e:
                print(e)
                print("Please try again!")
                

class FinanceTracker:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, transaction):                    #We can pass either an object or individual variables as the 2nd parameter
        self.transactions.append(transaction)
    
    def list_transaction(self):
        if not self.transactions:
            print("Oops! There are no transactions yet! ")
        else:
            print("List of transactions:")
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. {transaction}")

    def transaction_summary(self):
        total_amount = 0
        transaction_count = 0

        for transaction in self.transactions:
            total_amount += transaction.amount
            transaction_count += 1

        if transaction_count > 0:
            average_amount = total_amount / transaction_count
        else:
            average_amount = 0

        print(f"Total amount spent: ${total_amount:.2f}")
        print(f"Average amount per transaction: ${average_amount:.2f}")
        print(f"Number of transactions: {transaction_count}")

    def file_save(self, filename):
        with open(filename, "w") as file:
            for transaction in self.transactions:
                file.write(f"{transaction.date} | {transaction.category} | {transaction.amount} | {transaction.description}\n")
            print("Transactions saved!")
    
    def file_load(self, filename):
        try:
            self.transactions = []
            with open(filename, "r") as file:
                for line in file:
                    date, category, amount, description = [part.strip() for part in line.split("|")]
                    transaction = Transaction(date, category, float(amount), description)
                    self.transactions.append(transaction) 
                print("Transactions loaded!")
        except FileNotFoundError:
            print(f"The file {filename} does not exist!")
    


#Main function to run the program
def main():
    finance_tracker = FinanceTracker()
    print("\nWelcome to the Finance tracker App! Here you can enter your transactions/costs to manage your day-to-day expenses.")
    while True:
        try:
            print("\nMain Menu: Please choose from the following options:")
            print("1. Add Transaction")
            print("2. List Transactions")
            print("3. View Summary")
            print("4. Save File")
            print("5. Load File")
            print("6. Exit")
            choice = input("# ")

            if choice == "6":
                print("You have chosen to quit the Finance tracker app. The app will now close!")
                break
            elif choice == "1":
                temp_transaction = Transaction(None, None, None, None)     #Creates a temp Transaction instance with parameters as None
                temp_transaction.validate()
                finance_tracker.add_transaction(temp_transaction)
            elif choice == "2":
             finance_tracker.list_transaction()
            elif choice == "3":
                finance_tracker.transaction_summary()
            elif choice == "4":
                finance_tracker.file_save("transactions.txt")
            elif choice == "5":
                finance_tracker.file_load("transactions.txt")
            else:
                print("Invalid task number! Please enter a valid number.")
        except ValueError:
            print("An exception occurred! Please enter a valid number.")


if __name__ == "__main__":
    main() 
        