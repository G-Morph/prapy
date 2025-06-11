''' Exercise 2.4 - 2.x '''

import csv


def read_portfolio(csv_file: str) -> list[dict[str, str|int|float]]:
    ''' parse/read portfolio csv file '''
    portfolio: list[dict[str, str|int|float]] = []
    with open(csv_file, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        # this pops the header line, prior knowledge of file needed for this stuff:
        header = next(rows)
        # now get to the actual data, from the second line on:
        for index, row in enumerate(rows):
            try:
                record = dict(zip(header, row))
                holding = {
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])}
                portfolio.append(holding)
            except ValueError as ve:
                raise ValueError(f"Row: {index}, couldn't convert: {row}") from ve
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


def print_header() -> None:
    ''' helper to print a beautiful header for print_report '''
    header = 'Name Shares Price Change'.split()
    border: str = '-' * 10
    print(f'{header[0]:>10} ' +
          f'{header[1]:>10} ' +
          f'{header[2]:>10} ' +
          f'{header[3]:>10}')
    print(border, border, border, border)


def print_report(report: list[tuple[str,int,float,float]]) -> None:
    ''' print a beautiful report '''
    print_header()
    for stock in report:
        # you have to 'pre-format' the string otherwise it won't center with the dollar sign:
        price = f'${stock[2]:.2f}'
        print(f'{stock[0]:>10s} ' +
              f'{stock[1]:>10d} ' +
              f'{price:>10} ' +  # this is where the dollar string would get messed up
              f'{stock[3]:>10.2f}')


if __name__ == "__main__":
    # READ PORTFOLIO
    portfolio_: list[dict[str, str|int|float]] = read_portfolio('Work\\Data\\portfolio.csv')
    # READ PRICES:
    stocks_: dict[str, float] = read_prices('Work\\Data\\prices.csv')
    # MAKE REPORT:
    report_: list[tuple[str, int, float, float]] = make_report(portfolio_, stocks_)
    # PRINT IT NICE:
    print_report(report_)
