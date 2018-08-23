
'''
The definition of your payment() function goes here.
Delete these comment lines
'''


def calculate_payment():
    prin = float(input("Principal Value> "))
    apr = float(input("APR> "))
    months = int(input("Number of months > "))

    monthly_payment = payment(prin, apr, months)
    interest = months * monthly_payment - prin
    interest = round(interest, 2)

    ''' Delete this line
    print("A loan of ${0:.0f} with an interest rate of {1:0.1f}% will require a monthly payment of ${2:.0f} in order to pay off the loan in {3:.0f} months.\nOver the lifetime of the loan, a total of ${4:.0f} will be paid in interest".format(prin, apr, monthly_payment, months, interest))
    ''' # Delete this line


# Do not change anything below this line
    
def main():
    calculate_payment()

main()
