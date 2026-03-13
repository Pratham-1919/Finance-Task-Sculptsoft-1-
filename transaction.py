import os
import csv
from datetime import date


class transaction:
    TransactionID = 1000
    @classmethod
    def history(cls,password, Amount, Expense_type: str):
        try:
            tranx_csv = "tranx.csv"
            file_exists = os.path.isfile(tranx_csv)
            timestamp = date.today()
            with open(tranx_csv,"a",newline="") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(['Password', 'Transaction ID', 'Expense Type', 'Amount','Date'])
                writer.writerow([password, cls.TransactionID,Expense_type, Amount, timestamp]) 
            cls.TransactionID = cls.TransactionID + 1

        except Exception as e:
            print(f"Error in saving the file: {e}")


    def transaction_monthly(self,password,month):
            try:
                tranx_csv = "tranx.csv"
                file_exists = os.path.isfile(tranx_csv)
                with open(tranx_csv,"r",newline="") as file:
                    if not file_exists:
                        print("No such file exists....")
                    else:
                        reader = csv.reader(file)
                        next(reader)
                        for row in reader:
                            month_csv = int(row[4].split('-')[1])
                            if password == row[0] and month_csv == month:
                                print(row)
                       
            except Exception as e:
                print(f"Error in reading the data: {e}")
            