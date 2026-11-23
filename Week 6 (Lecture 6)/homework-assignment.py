class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        return self.balance

def log_transaction(message):
    try:
        with open("transactions.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except IOError:
        print("Log file error.")

def run_simulator():
    account = Account(100)
    while True:
        try:
            print("\n1. Deposit\n2. Withdraw\n3. Exit")
            choice = input("Choose option: ")
            if choice == "3":
                break
            elif choice in ["1", "2"]:
                amount_str = input("Enter amount: ")
                try:
                    amount = float(amount_str)
                except ValueError:
                    raise InvalidAmountError("Numeric input required.")
                
                if choice == "1":
                    new_bal = account.deposit(amount)
                    log_transaction(f"Deposit: {amount}, Balance: {new_bal}")
                else:
                    new_bal = account.withdraw(amount)
                    log_transaction(f"Withdraw: {amount}, Balance: {new_bal}")
            else:
                print("Unsupported menu option.")
        except InvalidAmountError as e:
            print(f"Error: {e}")
        except InsufficientFundsError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"System error: {e}")
        else:
            print("Transaction successful.")
        finally:
            print("Process finished.")

run_simulator()