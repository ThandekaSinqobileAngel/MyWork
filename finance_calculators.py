#Capstone Project
#This program is for a small financial company, that allows the user to access two diferent financial callculators.
#The two calculators are investment calculator ana home loan calculator.
#The user chooses which calulator to use.
#Based on the users input, furthur series of questions are asked.
#Calculations are then made
#Dependant on the users answers the desired amount are displayed.


import math

first_output = ("""Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment\t -to calculate the amount of interest you'll earn on interest\n
bond\t\t -to calculate the amount you'll have to pay on a home loan\n""")
print(first_output)

calculator_type = input(" ")

invest_low = "investment"
invest_up = invest_low.upper()

bond_low = "bond"
bond_up = bond_low.upper()

if (calculator_type == invest_low or calculator_type == invest_up):
    deposit = int(input("Enter your depost amount: "))
    investment_intest_rate = int(input("Enter interest rate(eg. 8 not 8%): "))
    years = int(input("Enter number of years you plan to invest for: "))
    interest_type = int(input("Enter interest type. \n1.Simple \n2.compound\n"))
    if(interest_type == 1):
        actual_rate = investment_intest_rate / 100
        amount = deposit*(1+actual_rate*years)
        print(f"The amount of interest is: {amount}")
        exit("For further calculations run the program again")
    elif(interest_type == 2):
        actual_rate = investment_intest_rate / 100
        amount = deposit * math.pow((1+actual_rate),years) 
        print(f"The amount of interest is: {amount}")
        exit("For further calculations run the program again")
else:
    print("Enter investment or INVESTMENT")
    
if (calculator_type == bond_low or calculator_type == bond_up):
    print("Enter present house value: ")
    house_value = float(input())
    print("Enter number of months to repay bond::")
    num_months = float(input())
    print("Enter interest rate(eg. 7 not 7%: ")
    bond_intest = float(input()) / 100 * (1/12)
    amount = house_value * ((bond_intest * ((1 + bond_intest) ** num_months)) / (((1 + bond_intest) ** num_months) - 1))
    print(f"Your monthly payment is {amount}")
    exit("For further calculations run the program again")
else:
    print("Enter bond or BOND")