''' Exercise 3.3 '''

import csv


def parse_csv(
    filename: str,
    select = None
    ) -> list:
    ''' parse a csv file into a list of records '''
    if select is None:
        select = ['name', 'shares']
    records = []
    with open(filename, encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row:
                record = dict(zip(headers, row))
                filtered_record = {}
                for key, value in record.items():
                    if key in select:
                        filtered_record[key] = value
                records.append(filtered_record)
    return records


if __name__ == "__main__":
    res = parse_csv(
        'Work/Data/portfolio.csv',
        select=['name', 'price'])
    for line in res:
        print(line)

    res = parse_csv(
        "Work/Data/portfolio.csv",
        select=['shares'])
    for line in res:
        print(line)

    res = parse_csv(
        "Work/Data/portfolio.csv"
    )
    for line in res:
        print(line)
