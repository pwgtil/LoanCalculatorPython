import math
import argparse


def init_check(args):
    ok = True
    if args.type not in ["annuity", "diff"]:
        ok = False
    if args.type == "diff" and args.payment is not None:
        ok = False
    if args.interest is None:
        ok = False
    if any(["-" in getattr(args, txt) for txt in vars(args) if getattr(args, txt) is not None]):
        ok = False
    if len([txt for txt in vars(args) if getattr(args, txt) is not None]) != 4:
        ok = False
    return ok


parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])  # mandatory
parser.add_argument("--payment")  # only for annuity
parser.add_argument("--principal")  # available for both
parser.add_argument("--periods")  # both
parser.add_argument("--interest")  # mandatory

args = parser.parse_args()

if not init_check(args):
    print("Incorrect parameters")
else:
    interest = float(args.interest)
    i = interest / 1200

    if args.type == 'annuity':
        case = [key for key in vars(args) if getattr(args, key) is None][0]
        p, a, n = 0.0, 0.0, 0
        if case == "periods":  # a, p
            p = float(args.principal)
            a = float(args.payment)
            n = math.ceil(math.log((a / (a - i * p)), 1 + i))
            years = n // 12
            months = n % 12
            txt_years = f'{years if years > 0 else ""}' + (" year" if years > 0 else "") + "s" if years > 1 else ""
            txt_and = " and " if years > 0 and months > 0 else ""
            txt_months = f'{months if months > 0 else ""}' + (
                " month" if months > 0 else "") + "s" if months > 1 else ""
            print(f'It will take {txt_years + txt_and + txt_months} to repay this loan!')
        elif case == "payment":  # p, n
            p = float(args.principal)
            n = int(args.periods)
            a = math.ceil(p * (i * (1 + i) ** n) / (((1 + i) ** n) - 1))
            print(f'Your annuity payment = {math.ceil(a)}!')
        elif case == "principal":  # a, n
            a = float(args.payment)
            n = int(args.periods)
            p = a / ((i * (1 + i) ** n) / (((1 + i) ** n) - 1))
            print(f'Your loan principal = {math.floor(p)}!')
        print("Overpayment = " + str(math.ceil(a * n - p)))
    elif args.type == 'diff':
        p = float(args.principal)
        n = int(args.periods)
        sum = 0
        for m in range(1, n + 1):
            d = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
            sum += d
            print(f"Month {m}: payment is {d}")
        print(f"\nOverpayment = {math.ceil(sum - p)}")
