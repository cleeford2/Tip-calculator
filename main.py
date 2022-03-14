#Tip Calculator 
print("Welcome to the tip calculator!")

#Total bill to pay.
bill = input("What was the total bill? $")

#Tip percentage willing to pay.
tip_giving = input("How much tip would you like to give? 10, 12, or 15? ")

#The bill split between
bill_split = input("How many people to split the bill? ")

#Tip percentage calculation
tip_percent = float(tip_giving) / 100 + 1

#Bill to pay including tip
tip_calculation = float(bill) / int(bill_split) * tip_percent

#round total mumber 2 decimals
print("Each person should pay: $", round(tip_calculation, 2))