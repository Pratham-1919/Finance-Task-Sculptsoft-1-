import csv
import os

class User:
    def __init(self,name,password,initial_balance=0):
        self.name = name,
        self.password = password,
        self.initial_balance = initial_balance,

    def new_account(self,name,password,initial_balance,account_type):
        User_csv = "user.csv"
        print("For new user")
        try:
            file_exists = os.path.isfile(User_csv)
            with open(User_csv,"a",newline="") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(['Name','Password','Initial balance','account_type'])
                writer.writerow([name,password,initial_balance,account_type])
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



