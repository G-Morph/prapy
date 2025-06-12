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


def parse_portfolio_csv(filepath: str) -> list:
    ''' split the CSV file into members '''
    records = []
    with open(filepath, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)
        header = next(rows)  # hopefully, there's a header!
        types = [str, int, float]  # for auto-casting later
        for index, row in enumerate(rows):
            if row:
                casted = [func(val) for func, val in zip(types, row)]
                record = dict(zip(header, casted))
                try:
                    records.append(record)
                except ValueError as ve:
                    raise ValueError(f"Row {index}: Couldn't convert: {row}") from ve
    return records

if __name__ == "__main__":
    print(parse_portfolio_csv('Work/Data/portfolio.csv'))
