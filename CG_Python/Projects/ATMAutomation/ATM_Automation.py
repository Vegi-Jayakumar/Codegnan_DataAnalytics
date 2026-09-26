# ATM Machine

'''
Technologies:
-> basic Python
    1.variables
    2.data types
    3.conditional statements
    4.Statements
    5.Operators

Components:
-> PIN Authentication
-> Balance Display
-> Withdrawal
-> Deposit
-> PIN Change
-> Statement
-> Exit
'''

#User database
user_details = {
    "Name" : "Jayakumar",
    "Address" : "123, ABC Street, Chennai",
    "Pancard No." : "ABCDE1234F",
    "PIN" : "1234",
    "Balance" : 20000.00,
    "Transactions" : []
}

# PIN Authentication
all_attempts = 3
while all_attempts > 0:
    entered_pin = input("Enter your 4-digit PIN : ")
    if len(entered_pin) == 4 and entered_pin in user_details["PIN"]:  #Checks if entered pin is the stored pin value
        print("\nWelcome to the ATM")
        entered_choice = int(input("\n\tChoose \n1.Withdraw\n2.Deposit\n3.Check balance\n4.PIN change\n5.Statement \n\nEnter Choice: "))    #Choice for options
        if entered_choice == 1 :    #Withdraw
            withdraw_amount = float(input("Enter the amount to withdraw : "))   #Withdrawal amount
            if withdraw_amount < user_details['Balance'] and withdraw_amount % 100 == 0 :
                user_details['Balance'] -= withdraw_amount  #Updating the balance
                user_details["Transactions"].append(f"Withdrawal : {withdraw_amount}")  #Record Transaction
                print("Take cash")
            else:
                print("Insufficient balance/Invalid Entry")
                break
            second_choice = int(input("\n\tChoose \n1.Home \n2.Exit \n\nEnter Choice: "))
            if second_choice == 2:
                break
        elif entered_choice == 2:   #Deposit
            deposit_amount = float(input("Enter amount to deposit : ")) #Deposit amount
            if deposit_amount % 100 == 0:
                user_details['Balance'] += deposit_amount   #Updating the balance
                user_details["Transactions"].append(f"Deposit : {deposit_amount}")  #Record Transaction
                print("Amount deposited")
            else:
                print("Invalid amount")
                break
            second_choice = int(input("\n\tChoose \n1.Home \n2.Exit \n\nEnter Choice: "))
            if second_choice == 2:
                break
        elif entered_choice == 3:   #Check balance
            print(f"Current Balance : {user_details['Balance']}")   #Displays current balance
            second_choice = int(input("\n\tChoose \n1.Home \n2.Exit \n\nEnter Choice: "))
            if second_choice == 2:
                break
        elif entered_choice == 4:   #Change PIN
            current_pin = input("Enter your current PIN : ")   #Checks the Current PIN
            if current_pin == user_details["PIN"]:
                new_pin = input("Enter your new PIN : ")   #Takes new PIN
                confirm_pin = input("Confirm your PIN : ")   #Confirm PIN
                if new_pin == confirm_pin:
                    user_details["PIN"] = new_pin   #Updating the PIN
                    print("PIN changed successfully")
                else:
                    print("PIN does not match")
            else:
                print("Invalid PIN")
                break
            second_choice = int(input("\n\tChoose \n1.Home \n2.Exit \n\nEnter Choice: "))
            if second_choice == 2:
                break
        elif entered_choice == 5:   #Statement
            print("\nStatement : \n")
            if len(user_details["Transactions"]) == 0:
                print("No transactions yet")
            else:
                print("Transactions: \n")
                count = 1
                for transaction in user_details["Transactions"][::-1]:
                    print(f"{count}. {transaction}")
                    count += 1
            second_choice = int(input("\n\tChoose \n1.Home \n2.Exit \n\nEnter Choice: "))
            if second_choice == 2:
                break
        else:
            print("\tInvalid Choice")
            break
    else:
        all_attempts -= 1
        if all_attempts > 0:    #Checks for number of attempts left
            print(f"You have {all_attempts} attempts left.")
        else:
            print("Your Card is blocked.")
print("Thank you for using the ATM")
