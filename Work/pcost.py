# pcost.py

''' Exercise 1.27 '''

import sys


class Porfolio():
    ''' stock portfolio stuff '''

    def __init__(self, portfolio_string: str):
        self.portfolio_string = portfolio_string
        self.parse_portfolio_string()

    records: list[tuple[str, int, float]] = []

    def parse_portfolio_string(self) -> None:
        ''' split the CSV file into members '''
        data_lines = self.portfolio_string.split('\n')
        header = tuple(data_lines[0].split(','))  # how to know if there's a header?
        for index, line in enumerate(data_lines[1:]):
            if line:
                record = dict(zip(header, line.split(',')))
                try:
                    name: str = record['name']
                    shares = int(record['shares'])
                    price = float(record['price'])
                    self.records.append((name, shares, price))
                except ValueError as ve:
                    raise ValueError(f"Row {index}: Couldn't convert: {line}") from ve

    def total_value(self) -> float:
        ''' total value from all shares '''
        total_value: float = 0
        for record in self.records:
            _, shares, stock_price = record
            total_value += stock_price * shares
        return total_value

    def print_portfolio(self) -> None:
        ''' print each stock's name, number of shares, and total value '''
        for record in self.records:
            name, shares, price = record
            print(f"{name:>10} {shares:^10} ${price:<10.2f}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        csvfile: str = sys.argv[1]
    else:
        #csvfile = 'Work/Data/portfolio.csv'
        #csvfile: str = 'Work/Data/missing.csv'
        csvfile: str = 'Work/Data/portfoliodate.csv'

    with open(csvfile, encoding='utf-8') as f:
        data_string: str = f.read()

    portfolio = Porfolio(data_string)
    portfolio.print_portfolio()
    portfolio_value: float = portfolio.total_value()
