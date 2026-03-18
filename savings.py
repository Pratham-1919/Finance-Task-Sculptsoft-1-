from account import bankaccount
from datetime import date
from user import User

class Savingsaccount(bankaccount):
    def __init__(self, interest_rate=0.045):
        self.interest_rate = interest_rate

    def get_account_type(self):
        return "Savings"

    def apply_monthly_update(self, password):
        balance = float(self.checkbalance(password))
        today = date.today()
        user = User()
        last_updated_date = user.get_last_update(password)
        today = date.today()
        months_passed = (today.year - last_updated_date.year) * 12 + (today.month - last_updated_date.month)
        if months_passed < 1:
            print("1 month not completed yet...")
        else:
            interest = balance * (self.interest_rate / 12) * months_passed
            self.deposit(password, interest)
            user.update_last_update(password)
            print(f"Interest of {interest:.2f} applied successfully for {months_passed} month(s).")

    def withdraw(self, password,amount,Description):
        try:
            if float(super().checkbalance(password)) - amount < 1000:
                raise Exception("Minimum balance required")

            super().withdraw(password,amount,Description)
        except Exception as e:
            print(f"{e}")
            pass

    
