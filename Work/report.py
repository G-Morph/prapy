# report.py
''' Exercise 2.4 - 2.x '''

import csv


def read_portfolio(csv_file: str) -> list[dict[str, str|int|float]]:
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
    return portfolio


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


def calculate_gain(  # should be called update_portfolio()
    portfolio: list[dict[str, str|int|float]],
    stocks: dict[str, float]
    ) -> tuple[float, float, float]:
    ''' did you lose some or win some? also, update portfolio with new prices '''
    prev_total: float = 0
    current_total: float = 0
    for holding in portfolio:
        # seems kludgey with all these float() casts
        # update prev total, for calculating gain/loss
        prev_total += float(holding['price']) * int(holding['shares'])
        if holding['name'] in stocks.keys():
            # update the holding dict with the new price
            holding['price'] = float(stocks[str(holding['name'])])
            # update current total with new price
            current_total += float(holding['price']) * int(holding['shares'])
    return (prev_total, current_total, current_total - prev_total)


# READ PORTFOLIO
portfolio_ = read_portfolio('Work\\Data\\portfolio.csv')
print(
    'Name' + '\t' +
    'Shares' + '\t' +
    'Price')
for holding_ in portfolio_:
    print(
        f'{holding_['name']}' + '\t' +
        f'{holding_['shares']}' + '\t' +
        f'${holding_['price']:.2f}')

# READ PRICES:
stocks_ = read_prices('Work\\Data\\prices.csv')
print(f'IBM:\t${stocks_['IBM']:.2f}')

# UPDATE AND CALCULATE GAIN:
prev_total_, current_total_, gain_ = calculate_gain(portfolio_, stocks_)
print(
    f'Previous total: ${prev_total_:.2f}' + '\n'
    f'Current total: ${current_total_:.2f}' + '\n'
    f'Gain: ${gain_:.2f}')
