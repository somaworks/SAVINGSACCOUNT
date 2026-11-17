#CQ13 - Intro to Classes
#Class 
class SavingsAccount:
    #Constructor Function???
    def __init__(self, accountid, balance, p_balance, interest_rate):
        self.account_id = accountid
        self.balance = balance
        self.p_balance = p_balance
        self.interest_rate = interest_rate 
        pass

    #SETTERS
    def set_interest_rate(self, new_interest_rate):
        self.interest_rate = new_interest_rate

    #GETTERS
    def get_monthly_rate(self):
        return self.interest_rate / 100 / 12

    def get_monthly_interest(self):
        return self.balance * self.get_monthly_rate()

    def get_balance_change(self):
        return ((self.balance - self.p_balance) / self.p_balance) * 100

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

def main():
    account = SavingsAccount(1122, 20_000.0, 18_500.0, 4.5)

    #WITHDRAWAL
    account.withdraw(2500.0)

    #DEPOSIT
    account.deposit(3000.0)

    #ACCOUNT OVERVIEW PRINTS
    print(f"Account ID: {account.account_id}")
    print(f"Current Balance: ${account.balance:.2f}")
    print(f"Monthly Interest Rate: {account.get_monthly_rate():.6f}")
    print(f"Monthly Interest: ${account.get_monthly_interest():.2f}")
    print(f"Percentage Change: {account.get_balance_change():.2f}%")

if __name__ == "__main__":
    main()
