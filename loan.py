from account import bankaccount
import csv
import os
from datetime import date

class LoanAccount(bankaccount):

    def __init__(self, account_id="", principal=0, emi=0, months=0):
        super().__init__(principal) 
        self.account_id = account_id
        self.principal = float(principal) if principal else 0
        self.emi_amount = float(emi) if emi else 0
        self.total_months = int(months) if months else 0
        self.remaining_months = int(months) if months else 0

    def extend_csv(self):
        rows = []
        if os.path.isfile("user.csv"):
            with open("user.csv", "r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader, [])
                if "principal" not in header:
                    header.extend(["principal", "emi", "remaining_months"])
                rows.append(header)
                for row in reader:
                    if len(row) == 6:
                        row.extend(["", "", ""]) 
                    rows.append(row)

            with open("user.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

    def calculate_emi(self, principal, rate, months):
        principal = float(principal)
        rate = float(rate)
        months = int(months)
        r = rate / 12 / 100
        emi = (principal * r * (1 + r) ** months) / ((1 + r) ** months - 1)
        return emi

    def save_loan(self, name):
        file_exists = os.path.isfile("user.csv")
        if file_exists:
            self.extend_csv()
        
        timestamp = date.today()
        with open("user.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'Password', 'Initial balance', 'account_type', 'Date', 'Last Update', 'principal', 'emi', 'remaining_months'])
            writer.writerow([name, self.account_id, self.principal, "loan", timestamp, timestamp, self.principal, self.emi_amount, self.remaining_months])