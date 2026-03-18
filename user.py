import csv
import os
from datetime import date

class User:
    def __init__(self,name=None,password=None,initial_balance=0):
        self.name = name
        self.password = password
        self.initial_balance = initial_balance

    def new_account(self,name,password,initial_balance,account_type):
        User_csv = "user.csv"
        print("For new user")
        try:
            file_exists = os.path.isfile(User_csv)
            timestramp = date.today()
            with open(User_csv,"a",newline="") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(['Name','Password','Initial balance','account_type','Date','Last Update'])
                writer.writerow([name,password,initial_balance,account_type,timestramp,timestramp])
        except Exception as e:
            print(f"Error in saving the file: {e}")



    def loged(self,password):
        with open("user.csv","r",newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[1].strip() == password.strip():
                    return True
            else:
                return False

    def get_account_type(self, password):
        with open("user.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[1].strip() == password.strip():
                    return row[3].strip().lower()
        return None
    


    def get_last_update(self,password):
        with open("user.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[1] == password:
                    date_str = row[5]
                    last_updated = date.fromisoformat(date_str)
                    return last_updated
            

    def update_last_update(self, password):
        rows = []
        today = date.today()

        with open("user.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row[1] == password:
                    row[5] = str(today)
                rows.append(row)

        with open("user.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
