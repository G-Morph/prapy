''' Exercise 3.3 '''

import csv


def parse_csv(filename: str) -> list:
    ''' parse a csv file into a list of records '''
    records = []
    with open(filename, encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row:
                record = dict(zip(headers, row))
                records.append(record)
    return records


if __name__ == "__main__":
    print(parse_csv(
        "Work/Data/portfolio.csv"
    ))
