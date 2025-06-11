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
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        print(
            f'{headers[0]}' + '\t' +
            f'{headers[1]}' + '\t' +
            f'{headers[2]}')
        for holding in portfolio:
            print(
                f'{holding[0]}' + '\t' +
                f'{holding[1]}' + '\t' +
                f'{holding[2]}')

read_portfolio('Work\\Data\\portfolio.csv')
