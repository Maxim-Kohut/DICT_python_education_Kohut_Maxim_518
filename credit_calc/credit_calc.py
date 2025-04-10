import math
import argparse
#---------------------------------------------
def raschet_diff(principal, srok_mes, procent_god):
    """
    Calc diff pays
    """
    # month perc rate
    procent_mes = procent_god / 1200
    # total pays
    vsego_plat = 0

    for mesyac in range(1, srok_mes + 1):
        # base part of pay
        osnovnaya_chast = principal / srok_mes
        # left debt
        ostatok_dolga = principal - (principal * (mesyac - 1)) / srok_mes
        # % for month
        procent_chast = ostatok_dolga * procent_mes
        # month pay (ceil up)
        platezh = math.ceil(osnovnaya_chast + procent_chast)

        vsego_plat += platezh
        print(f"Month {mesyac}: Pays {platezh} ")

    # Overpay
    pereplata = vsego_plat - principal
    print(f"\nOverpay: {pereplata} ")
#---------------------------------------------------------------------------------

def raschet_annuitet(principal, srok_mes, procent_god):
    """
    Calc annuitet pay
    """
    # mth rate
    procent_mes = procent_god / 1200

    # annuitet formula
    chislitel = procent_mes * math.pow(1 + procent_mes, srok_mes)
    znamenatel = math.pow(1 + procent_mes, srok_mes) - 1
    platezh = math.ceil(principal * chislitel / znamenatel)

    vsego_plat = platezh * srok_mes
    pereplata = vsego_plat - principal

    print(f"\nMonth pay: {platezh}")
    print(f"Ovrpay: {pereplata}")
#---------------------------------------------------------------------------------

def raschet_principal(platezh, srok_mes, procent_god):
    """
    Calc loan sum by pay
    """
    # month %
    procent_mes = procent_god / 1200

    # revers ann formula
    chislitel = procent_mes * math.pow(1 + procent_mes, srok_mes)
    znamenatel = math.pow(1 + procent_mes, srok_mes) - 1

    # get princ from pay
    principal = math.floor(platezh / (chislitel / znamenatel))

    vsego_plat = platezh * srok_mes
    pereplata = vsego_plat - principal

    print(f"\nLoan sum: {principal}")
    print(f"Ovrpay: {pereplata}")
#---------------------------------------------------------------------------------


def raschet_sroka(principal, platezh, procent_god):
    """
    Calc how long loan go
    """
    # month %
    procent_mes = procent_god / 1200

    try:
        # log formula 4 time
        srok_mes = math.log(
            platezh / (platezh - procent_mes * principal),
            1 + procent_mes
        )
    except (ValueError, ZeroDivisionError): #add except
        print("Err: pay too low")
        return

    srok_mes = math.ceil(srok_mes)

    # conv monts to yrs + mnths
    let = srok_mes // 12
    mes = srok_mes % 12

    # make str for dur
    srok_text = []
    if let > 0:
        srok_text.append(f"{let} yr{'s' if let != 1 else ''}")
    if mes > 0:
        srok_text.append(f"{mes} mth{'s' if mes != 1 else ''}")
    srok = " + ".join(srok_text)

    vsego_plat = platezh * srok_mes
    pereplata = vsego_plat - principal

    print(f"\nLoan dur: {srok}")
    print(f"Ovrpay: {pereplata}")
#---------------------------------------------------------------------------------


def check_args(args):
    """
    Check if args r ok
    """
    # chk loan type
    if args.type not in ["annuity", "diff"]:
        return False

    # % rate must be
    if args.interest is None or args.interest < 0:
        return False

    # no neg nums
    nums = [args.principal, args.payment, args.periods]
    if any(x is not None and x < 0 for x in nums):
        return False

    # 4 diff need princ + time
    if args.type == "diff":
        if args.payment is not None:
            return False
        if args.principal is None or args.periods is None:
            return False

    # 4 annuit need 2 of 3 params
    else:
        known = sum(1 for x in [args.principal, args.payment, args.periods] if x is not None)
        if known != 2:
            return False

    return True
#------------------------------------

def main():
    # set argum parser
    parser = argparse.ArgumentParser(description="Credit calc tool")

    # loan type: annu or diff
    parser.add_argument("--type", choices=["annuity", "diff"], required=True, help="Pay type")

    # how much take
    parser.add_argument("--principal", type=float, help="Loan sum")

    # mth pay
    parser.add_argument("--payment", type=float, help="Pay each month")

    # time in months
    parser.add_argument("--periods", type=int, help="How long")

    # % no sign
    parser.add_argument("--interest", type=float, help="Year rate (no %)")

    args = parser.parse_args()

    if not check_args(args):
        print("Error in params")
        return

    if args.type == "diff":
        # run diff calc (pay change each mth)
        raschet_diff(args.principal, args.periods, args.interest)
    else:
        # princ + time - calc fix pay
        if args.principal and args.periods:
            raschet_annuitet(args.principal, args.periods, args.interest)

        # pay + time- find princ
        elif args.payment and args.periods:
            raschet_principal(args.payment, args.periods, args.interest)

        # princ + pay- get how long
        elif args.principal and args.payment:
            raschet_sroka(args.principal, args.payment, args.interest)
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()