from user import User
from account import Account
from transaction import transaction
from exception import FinanceException

def main():
    while True:
        print("Select 1 for login and 2 for register 3 for break")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                validate = input("Enter password: ")
                user = User()
                output = user.loged(validate)
                if output:
                    print("Login successful: ")
                    while True:
                        print("\n Options you can prefer: ")
                        print("\n 1 for Depositing money: ")
                        print("\n 2 for Withdraw money: ")
                        print("\n 3 Check balance: ")
                        print("\n 4 get complete transaction history: ")
                        print("\n 5 Get monthly transaction report: ")
                        print("\n 6 Exit: ")
                        
                        option = input("Mention your choice: ")
                        if option == "4":
                            print("Your Complete transaction history with total balance: ")
                            account = Account()
                            account.get_accounthistory(validate)
                        elif option == "1":
                            amount = input("Enter the amount you want to deposit: ")
                            amount = float(amount)
                            account = Account()
                            print(amount)
                            if amount<0:
                                print("Invalid data")
                            else:
                                account.deposit(validate,amount)
                        elif option == "2":
                            amount = float(input("Enter the amount you want to Withdraw: "))
                            Description = input("Enter the Description of the expense: ")
                            account = Account()
                            if amount<0 or amount > float(account.checkbalance(validate)):
                                print("Invalid data")
                            else:
                                account.withdraw(validate,amount,Description)
                        elif option == "3":
                            account = Account()
                            balance = account.checkbalance(validate)
                            print(balance)
                        elif option == "5":
                            account = Account()
                            date = int(input("Enter the month bethween 1-12 to get the transaction report: "))
                            transction = transaction()
                            transction.transaction_monthly(validate,date)
                           

                        else:
                            print("Invalid Input")
                            break
                else: 
                    print("Invalid password: ")


            elif choice == "2":
                name = input("Enter your name: ")
                account_type = input("Enter your account type saving or current: ")
                password = input("Enter your password: ")
                initial_balance = int(input("Enter the initial balance: "))


                user = User()
                user.new_account(name,password,initial_balance,account_type)
            else:
                print("Invalid details") 
                break

        except FinanceException as e:
            print(f"error: {e}")
        except ValueError:
            print(f"Invalid Input format: ")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
