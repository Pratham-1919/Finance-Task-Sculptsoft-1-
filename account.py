from abc import ABC,abstractmethod
from transaction import transaction
import csv

class Account(ABC):
    transactionID = 1000
    def deposit(self,password,amount):
        rows = []
        with open("user.csv","r",newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)
            for row in reader:  
                if row[1] == password:
                    row[2] = str(float(row[2]) + amount)

                rows.append(row)

        with open("user.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        keyword = "Deposit"
        transaction.history(password,amount,keyword)
    
    def checkbalance(self,password):
        with open("user.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[1] == password:
                    return row[2]
                
    def withdraw(self,password,amount,description):
        rows = []
        with open("user.csv","r",newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)
            for row in reader:
                if row[1] == password:
                    row[2] = str(float(row[2]) - amount)
                rows.append(row)

        with open("user.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        transaction.history(password,amount,description)

    def get_accounthistory(self,password):
        with open("tranx.csv","r",newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == password:
                    print(row)
    

        

        
            


        

