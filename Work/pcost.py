# pcost.py

''' Exercise 1.27 '''

import os
import sys
import textwrap


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


# TODO: USE TEXTWRAP TO FIX ALL THE STUPID FORMATTING BULLSHIT


    def total_value(self) -> float:
        ''' total value from all shares '''
        total_value: float = 0
        for record in self.records:
            _, _, stock_price = record
            total_value += stock_price
        # :.2f formats float string to 2 decimal places with 0 fill:
        #print(f"Total value:\t\t\t${round(total_value, 2):.2f}")
        res = textwrap.shorten(f"Total value: ${round(total_value, 2):.2f}", width=24)
        print(res)
        return total_value

    def print_portfolio(self) -> None:
        ''' print each stock's name, number of shares, and total value '''
        for record in self.records:
            name, shares, price = record
            print(f"{name}\t\t{shares}\t\t${price:.2f}")


CWD: str = os.getcwd()
CSVFILE: str = ""
if len(sys.argv) == 2:
    CSVFILE = sys.argv[1]
else:
    CSVFILE = CWD + '\\Work\\Data\\portfolio.csv'

with open(CSVFILE, encoding='utf-8') as csvfile:
    data_string: str = csvfile.read()

portfolio = Porfolio(data_string)
portfolio.print_portfolio()
portfolio_value: float = portfolio.total_value()
