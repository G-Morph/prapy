# mortgage.py
''' Exercise 1.7 - 1.11 '''


class Mortgage():
    ''' handle and display mortgage details '''
    principal: float = 500_000
    rate: float = 0.05
    payment: float = 3_684.11
    total_paid: float = 0
    months: int = 0

    def calculate_principal(self) -> float:
        ''' calculate new principal based on mortgage rate and monthly payment '''
        interest: float = 1 + (self.rate / 12)  # divide the annual rate by month
        return self.principal * interest - self.payment

    def make_payment(self) -> None:
        ''' handle monthly mortgage payments '''
        self.principal = self.calculate_principal()
        self.months += 1
        if self.months == 12:
            self.payment -= 1_000
        self.total_paid += self.payment

    def pay_off_deets(self) -> None:
        ''' calculate total money and time to pay off house '''
        while house.principal > 0:
            house.make_payment()
        print(f'${house.total_paid:,.2f} in {house.months} months')

house = Mortgage()
house.pay_off_deets()
