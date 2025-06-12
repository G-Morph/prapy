''' showcasing how everything in Python is a "first-class" object '''

import csv
import math


TYPE, VALUE = (0, 1)


objects = [abs, math, ValueError]
print(objects)

great_number: int = -420
abs_res: int = objects[0](great_number)
print(abs_res)

it_takes: int = 2
famous_number: float = objects[1].sqrt(it_takes)
print(famous_number)

try:
    # pylint: disable=invalid-name
    x = int("obvo not an integer")
    # pylint: enable=invalid-name
except objects[2] as ve:
    print(ve)


def parse_portfolio_string(filepath: str) -> list:
    ''' split the CSV file into members '''
    records = []
    with open(filepath, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        header = next(rows)
        types = [str, int, float]
        for index, row in enumerate(rows):
            if row:
                values = zip(types, row)
                record = dict(zip(header, values))
                try:
                    name = record['name'][TYPE](record['name'][VALUE])  # cast as string
                    shares = record['shares'][TYPE](record['shares'][VALUE])  # cast as int
                    price = record['price'][TYPE](record['price'][VALUE])  # cast as float
                    records.append((name, shares, price))
                except ValueError as ve:
                    raise ValueError(f"Row {index}: Couldn't convert: {row}") from ve
    return records

print(parse_portfolio_string('Work/Data/portfolio.csv'))
