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


def update_portfolio(
    portfolio: list[dict[str, str|int|float]],
    stocks: dict[str, float]
    ) -> None:
    ''' update portfolio with new prices '''
    for holding in portfolio:
        if holding['name'] in stocks.keys():
            # update the holding dict with the new price
            holding['price'] = float(stocks[str(holding['name'])])


def make_report(
    portfolio: list[dict[str, str|int|float]],
    stocks: dict[str, float]
    ) -> list[tuple[str, int, float, float]]:
    ''' print out a report on stock price changes within a specific portfolio '''
    reports: list[tuple[str, int, float, float]] = []
    for holding in portfolio:
        if holding['name'] in stocks.keys():
            name = str(holding['name'])
            shares = int(holding['shares'])
            old_price = float(holding['price'])
            new_price = float(stocks[name])
            reports.append((name, shares, new_price, round(new_price - old_price, 2)))
    return reports


# READ PORTFOLIO
portfolio_ = read_portfolio('Work\\Data\\portfolio.csv')

# READ PRICES:
stocks_ = read_prices('Work\\Data\\prices.csv')

# UPDATE AND CALCULATE GAIN:
#prev_total_, current_total_, gain_ = calculate_gain(portfolio_, stocks_)
#print(
#    f'Previous total: ${prev_total_:.2f}' + '\n'
#    f'Current total: ${current_total_:.2f}' + '\n'
#    f'Gain: ${gain_:.2f}')

# MAKE REPORT
reports_ = make_report(portfolio_, stocks_)
header = 'Name Shares Price Change'.split()
border: str = '-' * 10
print(f'{header[0]:>10} ' +
      f'{header[1]:>10} ' +
      f'{header[2]:>10} ' +
      f'{header[3]:>10}')
print(border, border, border, border)
for report_ in reports_:
    # you have to 'pre-format' the string otherwise it won't center with the dollar sign:
    price = f'${report_[2]:.2f}'
    print(f'{report_[0]:>10s} ' +
          f'{report_[1]:>10d} ' +
          f'{price:>10} ' +  # this is where the dollar string would get messed up
          f'{report_[3]:>10.2f}')
