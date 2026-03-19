from account import bankaccount
from user import User
from current import Current
from savings import Savingsaccount
import csv
import os
from datetime import date
from transaction import transaction

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


    def pay_emi(self, loan_password, payment_password):
        emi_amount = 0
        loan_found = False
        
        with open("user.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) >= 9 and row[1] == loan_password and row[3] == "loan":
                    loan_found = True
                    emi_amount = float(row[7])
                    remaining_months = int(row[8])
                    if remaining_months <= 0:
                        raise Exception("No remaining EMI to pay.")
                    break
                    
        if not loan_found:
            raise Exception("Loan account not found.")

        
        
        user_obj = User()
        payment_acc_type = user_obj.get_account_type(payment_password)
        if not payment_acc_type:
            raise Exception("Payment account not found or invalid password.")
            
        if payment_acc_type == "current":
            payment_acc = Current()
        elif payment_acc_type in ["saving", "savings"]:
            payment_acc = Savingsaccount()
        else:
            raise Exception("EMI can only be paid from Savings or Current accounts.")
            
        payment_acc.withdraw(payment_password, emi_amount, "EMI Payment")

        rows = []
        with open("user.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 9 and row[1] == loan_password and row[3] == "loan":
                    row[8] = str(int(row[8]) - 1)
                    row[2] = str(float(row[2]) - emi_amount)
                rows.append(row)

        with open("user.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            
        transaction.history(loan_password, emi_amount, "EMI Deduction")
        print(f"Successfully deducted EMI of {emi_amount:.2f} from your {payment_acc_type} account and updated loan details.")

    def loan_summary(self, password):
        with open("user.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) >= 9 and row[1] == password and row[3] == "loan":
                    return {
                        "Remaining Balance": float(row[2]),
                        "Original Principal": float(row[6]),
                        "EMI Amount": float(row[7]),
                        "Remaining Months": int(row[8])
                    }
        return None