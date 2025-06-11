# report.py
''' Exercise 2.4 '''

import csv


def read_portfolio(filename: str) -> None:
    ''' parse/read portfolio csv file '''

    portfolio = []

    with open(filename, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                headers[0]: row[0],
                headers[1]: row[1],
                headers[2]: row[2]}
            portfolio.append(holding)

    for holding in portfolio:
        print(holding)

read_portfolio('Work\\Data\\portfolio.csv')
