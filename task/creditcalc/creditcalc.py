import math

loan_principal = int(input('Enter the loan principal:\n'))
choice = input('What do you want to calculate\n\
type "m" - for number of monthly payments,\n\
type "p" - for the monthly payment:\n')
if choice == 'm':
    monthly_payment = int(input('Enter the monthly payment:\n'))
    result = math.ceil(loan_principal / monthly_payment)
    print(f'\nIt will take {result} months to repay the loan'
          if result > 1 else '\nIt will take 1 month to repay the loan')
else:
    no_of_months = int(input('Enter the number of months:\n'))
    payment = math.ceil(loan_principal / no_of_months)
    if loan_principal % no_of_months == 0:
        print(f'\nYour monthly payment = {payment}')
    else:
        last_payment = loan_principal - (no_of_months - 1) * payment
        print(f'\nYour monthly payment = {payment}  and the last payment = {last_payment}.')
