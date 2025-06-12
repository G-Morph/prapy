''' Exercise 3.3 - 3.x '''

import csv


def parse_csv(
    filename: str,
    select: list[str] | None = None,
    types: list[type] | None = None
    ) -> list[dict]:
    ''' parse a csv file into a list of records '''

    if select is None:
        select = ['name', 'shares']
    if types is None:
        types = [str, int, float]

    records = []  # the output list

    with open(filename, encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)  # hopefully, there's a header row!
        for row in rows:
            if row:  # if not a blank line in the csv file
                if types:  # if you need to cast strigs from the file
                    # each col of the row is the arg for type() casting
                    row = [typecast(col) for typecast, col in zip(types, row)]
                # make a dict of each row:
                raw_record = dict(zip(headers, row))
                # now make a new dict filtered by the select list arg:
                filtered_record = {}
                for key, value in raw_record.items():
                    # if it's one of the parameters (col) you want:
                    if key in select:
                        # add it to the record you'll return
                        filtered_record[key] = value
                # append it to the output list:
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
