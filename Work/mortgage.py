# mortgage.py
''' Exercise 1.7 '''


principal: float = 500_000.0
rate: float = 0.05
payment: float = 2684.11
total_paid: float = 0.0

while principal > 0:
    principal *= (1 + (rate / 12)) - payment
    total_paid += payment

print(f'Total paid: {total_paid}')
