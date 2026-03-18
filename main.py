from user import User
from account import bankaccount
from savings import Savingsaccount
from transaction import transaction
from exception import FinanceException
from loan import LoanAccount
from current import Current

def main():
    while True:
        print("Select 1 for login and 2 for register 3 for loan 4 for break")
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
                        print("\n 6 Apply monthly interest (Savings only): ")
                        print("\n 7 Apply monthly updates in current account: ")
                        print("\n 8 Exit: ")
                        
                        option = input("Mention your choice: ")
                        if option == "4":
                            print("Your Complete transaction history with total balance: ")
                            account = bankaccount()
                            account.get_accounthistory(validate)
                        elif option == "1":
                            amount = input("Enter the amount you want to deposit: ")
                            amount = float(amount)
                            account = bankaccount()
                            print(amount)
                            if amount<0:
                                print("Invalid data")
                            else:
                                account.deposit(validate,amount)
                        elif option == "2":
                            amount = float(input("Enter the amount you want to Withdraw: "))
                            Description = input("Enter the Description of the expense: ")
                            account_type = user.get_account_type(validate)
                            account = bankaccount()
                            if account_type in ["current"]:
                                current_acc = Current()
                                current_acc.withdraw(validate, amount,Description)
                            else:
                                savings_account = Savingsaccount()
                                savings_account.withdraw(validate,amount,Description)


                        elif option == "3":
                            account = bankaccount()
                            balance = account.checkbalance(validate)
                            print(balance)
                        elif option == "5":
                            account = bankaccount()
                            date = int(input("Enter the month bethween 1-12 to get the transaction report: "))
                            transction = transaction()
                            transction.transaction_monthly(validate,date)
                        elif option == "6":
                            account_type = user.get_account_type(validate)
                            if account_type in ["saving", "savings"]:
                                savings_acc = Savingsaccount()
                                savings_acc.apply_monthly_update(validate)
                            else:
                                print("Error: Interest can only be applied to a Savings account.")

                        elif option == "7":
                            break
                        
                        else:
                            print("Invalid Input")
                            break
                else: 
                    print("Invalid password: ")


            elif choice == "2":
                name = input("Enter your name: ")
                account_type = input("Enter your account type saving or current: ").lower()
                password = input("Enter your password: ")
                initial_balance = int(input("Enter the initial balance: "))

                user = User(name, password, initial_balance)
                user.new_account(name,password,initial_balance,account_type)
                account = bankaccount(initial_balance)

            elif choice == "3":
                print("This is your loan account...")
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                initial_balance = input("Enter the amount of loan you want: ")
                months = input("Enter tha number of months you will repay the loan: ")
                rate = 11
                principle = initial_balance
                emi = LoanAccount()
                emi_calculator = emi.calculate_emi(principle, rate, months)
                loan = LoanAccount(password, principle, emi_calculator,months)
                loan.save_loan(name)
                print(f"Loan account created successfully! Monthly EMI is {emi_calculator:.2f}")

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
