import math

# Below our first initial contact with user, giving print statements before requesting input
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")

print("investment     - to calculate the amount of interest you'll earn on interest")
print("bond           - to calculate the amount of interest you'll earn on interest\n")

calc = input().lower() # Used .lower() to account for variations in capitalization

# Our first block represents the input values and variables for the investment choice
# Once all our input has been received and stored we start our calculation

if calc == "investment":
    print("\nThank you for selecting investment:\n")
    print("Please tell us how much you'll be depositing:\n")
    deposit = float(input())
    print("\nThank you, please let us know the interest rate of your investment:\n")
    rate = float(input()) / 100
    print("\nThank you, please tell us for how many years you'd like to invest for:\n")
    years = int(input())
    print("\nThank you, finally, please tell us which interest format you'd like:\n")
    interest = input().lower()

# Below the calculation for either simple or compound interest input from user.
# Also included .is_integer() to make the output look neat if there are no decimals
# in the output value, and included a reduction to two decimals for cent value if
# output had more than 2 decimals once calculated.

    if interest == "simple":
        total_investment = deposit * (1 + rate * years)
        if total_investment.is_integer():
            total_investment = int(total_investment)  
        print("Your total investment will amount to R{:.2f}!".format(total_investment))
        
    elif interest == "compound":
        total_investment = deposit * math.pow((1 + rate), years)
        if total_investment.is_integer():
            total_investment = int(total_investment)
        print("Your total investment will amount to R{:.2f}!".format(total_investment))

    else:
        print("Sorry, that's not a valid interest format!") # Account for incorrect input
    
# Next block of conditionals will provide receiving user input for bond choice

elif calc == "bond":
    print("\nThank you for selecting bond:\n")
    print("Please tell us how much is your current house value:\n")
    value = float(input())
    print("\nThank you, please let us know what is your annual interest rate:\n")
    rate = float(input()) / 100
    print("\nThank you, finally, please tell us how many months you have left to pay:\n")
    time_left = int(input())

# Calculation below for bond repayment monthly rate as well as .is_integer and {.2f} for neat output.

    monthly_payment = ((rate / 12) * value) / (1 - (1 + (rate/12)) ** (-time_left))
    if monthly_payment.is_integer():
            monthly_payment = int(monthly_payment)
    print("Your monthly repayment amount will be R{:.2f}!".format(monthly_payment))
    
else:
    print("You've entered the incorrect calculation option") # Last conditional for incorrect choice
