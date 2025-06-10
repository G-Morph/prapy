# mortgage.py
''' Exercise 1.7 - 1.11 '''


class Mortgage():
    ''' handle and display mortgage details '''
    principal: float = 500_000
    rate: float = 0.05
    payment: float = 2_684.11
    total_paid: float = 0
    months: int = 0
    extra_payment_start_month: int = 0
    extra_payment_end_month: int = 12
    extra_payment: float = 1_000

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
        self.principal = self.calculate_principal()
        self.months += 1
        self.total_paid += self.payment

    def pay_off_deets(self) -> None:
        ''' calculate total money and time to pay off house '''
        while self.principal > 0:
            self.make_payment()
        print(f'${self.total_paid:,.2f} in {self.months} months')

    def adjust_payment(self):
        ''' calculate mortgage data based on adjusting monthly payments '''
        adjusted_house = Mortgage()
        adjusted_house.extra_payment = float(input(
            "how much would you like to adjust the monthly payment by? "))
        adjusted_house.extra_payment_start_month = int(input(
            "what number month would you like to start new payment amount? "))
        adjusted_house.extra_payment_end_month = int(input(
            "what number month would you like to end new payment amount? "))
        adjusted_house.pay_off_deets()

house = Mortgage()
house.pay_off_deets()
house.adjust_payment()
