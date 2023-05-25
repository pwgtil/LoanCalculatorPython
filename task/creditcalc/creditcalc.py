import math

choice = input('What do you want to calculate?\n\
type "n" - for number of monthly payments,\n\
type "a" for annuity monthly payment amount,\n\
type "p" for loan principal:\n')
if choice == 'n':
    loan_principal = int(input('Enter the loan principal:\n'))
    monthly_payment = float(input('Enter the monthly payment:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))
    monthly_interest = loan_interest / 1200
    payments = math.ceil(
        math.log((monthly_payment / (monthly_payment - monthly_interest * loan_principal)), 1 + monthly_interest))
    years = payments // 12
    months = payments % 12
    txt_years = f'{years if years > 0 else ""}' + (" year" if years > 0 else "") + "s" if years > 1 else ""
    txt_and = " and " if years > 0 and months > 0 else ""
    txt_months = f'{months if months > 0 else ""}' + (" month" if months > 0 else "") + "s" if months > 1 else ""
    print(f'It will take {txt_years + txt_and + txt_months} to repay this loan!')

elif choice == 'a':
    loan_principal = int(input('Enter the loan principal:\n'))
    no_of_periods = int(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))
    monthly_interest = loan_interest / 1200
    payment = loan_principal * (monthly_interest * (1 + monthly_interest) ** no_of_periods) / \
              (((1 + monthly_interest) ** no_of_periods) - 1)
    print(f'\nYour monthly payment = {math.ceil(payment)}!')
else:
    annuity_payment = float(input('Enter the annuity payment:\n'))
    no_of_periods = int(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))
    monthly_interest = loan_interest / 1200
    result = annuity_payment / ((monthly_interest * (1 + monthly_interest) ** no_of_periods) /
                                (((1 + monthly_interest) ** no_of_periods) - 1))
    print(f'\nYour loan principal = {round(result)}!')
