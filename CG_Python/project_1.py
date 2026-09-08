# ATM Machine

'''
Technologies:
-> basic Python
    1.variables
    2.data types
    3.conditional statements
    4. Statements

Components:
-> PIN Authentication
-> Balance Display
-> Withdrawal
-> Deposit
-> PIN Change
-> Mini Statement (last 3 transactions)
-> Exit
'''

user_details = {
    "Name" : "Jayakumar",
    "Address" : "123, ABC Street, Chennai",
    "Pancard No." : "ABCDE1234F",
    "PIN" : "1234",
    "Balance" : 20000.00
}

Transactions = []

# PIN Authentication
all_attempts = 3
while all_attempts > 0:
    entered_pin = input("Enter your 4-digit PIN : ")
    if entered_pin in user_details["PIN"]:  #Checks if entered pin is the stored pin value
        print("\nWelcome to the ATM")
        entered_choice = int(input("\n\tChoose \n1.Withdraw\n2.Deposit\n3.Check balance\n4.PIN change\n5.Mini Statement\n6.Exit \n\nEnter Choice: "))    #Choice for options
        if entered_choice == 1 :    #Withdraw
            withdraw_amount = float(input("Enter the amount to withdraw : "))   #Withdrawal amount
            if withdraw_amount < user_details['Balance'] and withdraw_amount % 100 == 0 :
                user_details['Balance'] -= withdraw_amount  #Updating the balance
                Transactions.append(f"Withdrawal : {withdraw_amount}")  #Record Transaction
                print("Take cash")
            else:
                print("Insufficient balance/Invalid Entry")
        elif entered_choice == 2:   #Deposit
            deposit_amount = float(input("Enter amount to deposit : ")) #Deposit amount
            if deposit_amount % 100 == 0:
                user_details['Balance'] += deposit_amount   #Updating the balance
                Transactions.append(f"Deposit : {deposit_amount}")  #Record Transaction
                print("Amount deposited")
            else:
                print("Invalid amount")
        elif entered_choice == 3:   #Check balance
            print(f"Current Balance : {user_details['Balance']}")   #Displays current balance
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
        elif entered_choice == 5:   #Mini Statement
            print("\nMini Statement : \n")
            if len(Transactions) == 0:
                print("No transactions yet")
            for transaction in Transactions[::-1]:    #Displays last 3 transactions in reverse order
                print(transaction)
        elif entered_choice == 6:   #Exit
            print("\tThank you for using ATM")
            break
        else:
            print("\tInvalid Choice")
    else:
        all_attempts -= 1
        if all_attempts > 0:    #Checks for number of attempts left
            print(f"You have {all_attempts} attempts left.")
        else:
            print("Your Card is blocked.")

