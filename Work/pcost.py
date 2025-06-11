# pcost.py

''' Exercise 1.27 '''

import sys


class Porfolio():
    ''' stock portfolio stuff '''

    def __init__(self, portfolio_string: str):
        self.portfolio_string = portfolio_string
        self.parse_portfolio_string()

    column_titles = None  # tuple of strings ('','','')
    records: list[tuple[str, int, float]] = []

    def parse_portfolio_string(self) -> None:
        ''' split the CSV file into members '''
        data_lines = data_string.split('\n')
        self.column_titles = tuple(data_lines[0].split(','))
        for line in data_lines[1:]:
            record_items = line.split(',')
            if len(record_items) == 3:
                try:
                    name: str = record_items[0]
                    shares = int(record_items[1])
                    price = float(record_items[2])
                    self.records.append((name, shares, price))
                except ValueError as ve:
                    raise ValueError("records should be: tuple[str, str, str]") from ve


    def total_value(self) -> float:
        ''' total value from all shares '''
        total_value: float = 0
        for record in self.records:
            _, shares, stock_price = record
            total_value += stock_price * shares
        #print(f"Total value:\t\t\t${round(total_value, 2):.2f}")
        return total_value

    def print_portfolio(self) -> None:
        ''' print each stock's name, number of shares, and total value '''
        for record in self.records:
            name, shares, price = record
            print(f"{name:^10} {shares:^10} ${price:^10.2f}")


CSVFILE: str = ""
if len(sys.argv) == 2:
    CSVFILE = sys.argv[1]
else:
    CSVFILE = 'Work\\Data\\portfolio.csv'

with open(CSVFILE, encoding='utf-8') as csvfile:
    data_string: str = csvfile.read()

portfolio = Porfolio(data_string)
portfolio.print_portfolio()
portfolio_value: float = portfolio.total_value()
