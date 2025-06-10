# mortgage.py
''' Exercise 1.7 - 1.11 '''

from copy import deepcopy


# TODO: comment everything while you still remember how it works
#       also, it looks like pylint doesn't like how many members
#       are part of the Mortgage class, does it need to be
#       simplified or broken up? check it nice

class Mortgage():
    ''' handle and display mortgage details '''
    def __init__(self, principal: float, rate: float, payment: float):
        self.principal = principal
        self.rate = rate
        self.payment = payment
        self.price: float = principal

    total_paid: float = 0
    months: int = 0
    extra_payment_start_month: int = 0
    extra_payment_end_month: int = 0
    extra_payment: float = 0

    def __str__(self) -> str:
        return (
            "\t" + f"price: {self.price}" + "\n" +
            "\t" + f"principal: {self.principal}" + "\n" +
            "\t" + f"rate: {self.rate}" + "\n" +
            "\t" + f"payment: {self.payment}" + "\n" +
            "\t" + f"extra_payment (ep): {self.extra_payment}" + "\n" +
            "\t" + f"ep start month: {self.extra_payment_start_month}" + "\n" +
            "\t" + f"ep end month: {self.extra_payment_end_month}" + "\n" +
            "\t" + f"months: {self.months}")

    def calculate_principal(self) -> float:
        ''' calculate new principal based on mortgage rate and monthly payment '''
        interest: float = 1 + self.rate / 12  # divide the annual rate by month
        return self.principal * interest - self.payment

    def make_payment(self) -> None:
        ''' handle monthly mortgage payments '''
        if self.months == self.extra_payment_start_month:
            self.payment += self.extra_payment
        elif self.months == self.extra_payment_end_month:
            self.payment -= self.extra_payment
        check_principal = self.calculate_principal()

        if check_principal < 0:
            self.payment = self.principal * (1 + self.rate / 12)

        self.principal = self.calculate_principal()

        self.total_paid += self.payment

        if (self.months in range(5)) or (self.principal < (self.payment * 4)):
            print(f'{self.months},' + '\t' +
                  f'{round(self.total_paid, 2):>10,.2f},' + '\t' +
                  f'{round(self.principal, 2):>10,.2f}')
            if self.months == 4:
                print('...')

        self.months += 1

    def pay_off_deets(self, from_principal: bool = False) -> None:
        ''' calculate total money and time to pay off house '''
        if from_principal:
            starting_amount: float = self.principal
            months = self.months
        else: # from price
            starting_amount: float = self.price
            months = 0
        paid_house = deepcopy(self)
        paid_house.principal = starting_amount
        paid_house.months = months
        while paid_house.principal > 0:
            paid_house.make_payment()
        print(
            f'Total: ${paid_house.total_paid:,.2f}' + '\n' +
            f'Years: {paid_house.months // 12}' + '\n' +
            f'Months: {paid_house.months % 12}')

    def adjust_payment(self, from_principal: bool = False):
        ''' calculate mortgage data based on adjusting monthly payments '''
        if from_principal:
            starting_amount: float = self.principal
        else: # from price
            starting_amount: float = self.price

        adjusted_house = Mortgage(starting_amount, self.rate, self.payment)

        adjusted_house.extra_payment = float(input(
            "how much would you like to adjust the monthly payment by? "))
        adjusted_house.extra_payment_start_month = int(input(
            "what number month would you like to start new payment amount? "))
        adjusted_house.extra_payment_end_month = int(input(
            "what number month would you like to end new payment amount? "))

        adjusted_house.pay_off_deets()

        decision: str = input(
            "Would you like to apply these changes?" + "\n")
        if decision.upper() in ('Y', 'YES'):
            self.extra_payment = adjusted_house.extra_payment
            self.extra_payment_start_month = adjusted_house.extra_payment_start_month
            self.extra_payment_end_month = adjusted_house.extra_payment_end_month
            print("Changes have been applied:")
            print(self)


original_house = (500_000, 0.05, 2684.11)
mortgage = Mortgage(*original_house)
mortgage.pay_off_deets()
mortgage.adjust_payment()
