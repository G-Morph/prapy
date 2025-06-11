# report.py
''' Exercise 2.4 - 2.x '''

import csv


def read_portfolio(csv_file: str) -> None:
    ''' parse/read portfolio csv file '''

    portfolio: list[dict[str, str|int|float]] = []

    with open(csv_file, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        # this pops the header line, prior knowledge of file needed for this stuff:
        next(rows)
        # now get to the actual data, from the second line on:
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])}
            portfolio.append(holding)
    # print it all out nice like:
    print(
        'Name' + '\t' +
        'Shares' + '\t' +
        'Price')
    for holding in portfolio:
        print(
            f'{holding['name']}' + '\t' +
            f'{holding['shares']}' + '\t' +
            f'${holding['price']:.2f}')

# call it to check it out:
read_portfolio('Work\\Data\\portfolio.csv')


def read_prices(csv_file: str) -> dict[str, float]:
    ''' read prices of other stocks in a csv file '''

    # 'name' = 'price'
    stocks: dict[str, float] = {}

    with open(csv_file, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        # no headers in this file (Work\Data\prices.csv)
        for row in rows:
            if row:  # 'name' = 'price'
                stocks[row[0]] = float(row[1])
    return stocks

# call it to check it out:
prices = read_prices('Work\\Data\\prices.csv')
