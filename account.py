from abc import ABC,abstractmethod
from transaction import transaction
import csv

class Account(ABC):
    def __init__(self,initial_balance=0):
        self._balance = float(initial_balance)

    @abstractmethod
    def deposit(self,password,amount):
        '''Here is the method to deposit the amount into the user account'''
        pass
   
    
    @abstractmethod
    def checkbalance(self,password):
        '''Here is the method to check the total balance of the user account'''
        pass
                
    @abstractmethod
    def withdraw(self,password,amount,description):
        '''Here is the method to withdraw the amount from the user account'''
        pass
    @abstractmethod
    def get_accounthistory(self,password):
        '''Get account summary'''
        pass


class bankaccount(Account):    
    def checkbalance(self, password):
        with open("user.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[1] == password:
                    return row[2]
                

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

    def withdraw(self,password,amount,desc, overdraft_limit=0):
        rows = []
        if amount<0 or (float(self.checkbalance(password)) - amount < overdraft_limit):                 
            raise ValueError
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
        
        transaction.history(password,amount,desc)

    def get_accounthistory(self,password):
        with open("tranx.csv","r",newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == password:
                    print(row)
    

        

        
            


        
