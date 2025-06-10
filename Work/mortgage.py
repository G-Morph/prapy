# mortgage.py
''' Exercise 1.7 - 1.11 '''


class Mortgage():
    ''' mortgage stuff, bro '''
    principal: float = 500_000
    rate: float = 0.05
    payment: float = 3_684.11
    total_paid: float = 0
    months: int = 0

    def calculate_principal(self) -> float:
        ''' helper to do math stuff '''        
        return self.principal * (1 + self.rate / 12) - self.payment

    def make_payment(self) -> None:
        ''' helper to return new principal after adjusting for rate and payment '''
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
