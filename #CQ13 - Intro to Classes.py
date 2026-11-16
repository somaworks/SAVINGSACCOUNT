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

    def balance_change(self):
        return ((self.balance - self.p_balance) / self.p_balance) * 100

    def Deposit(self, amount_out):
        if amount_out > balance:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - amount_out

    def Withdrawal(self, amount_out):
        self.balance = self.balance + amount_out

#Function
account = SavingsAccount(1222, 20_000.0, 18_500.0, 4.5)

#ACCOUNT OVERVIEW PRINTS
    print(f"Your Account ID: {account.accountid}")
    print(f"Your Current Balance: {account.balance}")
    print(f"Your Current Interest Rate: {account.interest_rate}")
    print(f"Your Current Monthly Interest Rate: {account.get_monthly_rate()}")
    print(f"Your Account Balance Change as a Percent is {account.balance_change()}")



def main():

if __name__ == "__main__":
    main()