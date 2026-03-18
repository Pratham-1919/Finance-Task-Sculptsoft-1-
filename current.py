from account import bankaccount

class Current(bankaccount):
    def __init__(self, over_draft_limit=200):
        self.overdraft_limit = over_draft_limit

    def get_account_type(self):
        return "Current"
    
    def withdraw(self, password,amount,desc):
        balance = float(self.checkbalance(password))
        if balance - amount < self.overdraft_limit:
            raise Exception("Overdraft limit exceeded")

        super().withdraw(password,amount,desc, self.overdraft_limit)