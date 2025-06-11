# report.py
''' Exercise 2.4 - 2.x '''

import csv


def read_portfolio(filename: str) -> None:
    ''' parse/read portfolio csv file '''

    portfolio: list[dict[str, str|int|float]] = []

    with open(filename, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                headers[0]: row[0],
                headers[1]: int(row[1]),
                headers[2]: float(row[2])}
            portfolio.append(holding)

    print(
        'Name' + '\t' +
        'Shares' + '\t' +
        'Price')
    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = holding['price']
        print(
            f'{name}' + '\t' +
            f'{shares}' + '\t' +
            f'${price:.2f}')

read_portfolio('Work\\Data\\portfolio.csv')
