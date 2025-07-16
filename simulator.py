
pin = 1234
balance = 1000

# prompt user to enter a pin
user_pin = int(input("Enter your pin.")) 

if user_pin == pin:
    print("Access granted")
    print("1. Check Balance")
    print("2. Withdraw Money")

    choice = input("Choose an option: ")
    if choice == '1':
     print("Your balance is Ksh", balance)

    elif choice == '2':
        amount = float (input("Enter amount to withdraw: "))
        if amount <= balance and amount > 0 :

            balance = balance - amount
            print("Withdraw successful. New balance:", balance)
        else:
            print("Insufficient funds")
    else:
     print("Invalid option")

else:
    print("Access denied. Wrong PIN")
