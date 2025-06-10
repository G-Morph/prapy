# sears.py
''' Exercise 1.6: Debugging '''


bill_thickness: float = 0.11 * 0.001    # Meters (0.11 mm)
sears_height: float = 442             # Height (meters)
num_bills: float = 1
day: int = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
