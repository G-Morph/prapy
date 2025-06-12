''' Exercise 3.3 - 3.x '''

import csv


def parse_csv(
    filename: str,
    has_header: bool = True,
    delimiter: str = ',',
    select: list[str] | None = None,
    types: list[type] | None = None
    ) -> list:
    ''' parse a csv file into a list of records '''

    if select is None:
        select = ['name', 'shares']
    if types is None:
        types = [str, int, float]

    records = []  # the output list

    with open(filename, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_header:
            headers = next(rows)
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
        else:  # no header
            for row in rows:
                if types:  # if you need to cast strigs from the file
                    # each col of the row is the arg for type() casting
                    row = [typecast(col) for typecast, col in zip(types, row)]
                records.append(row)
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

    # for a csv file with no headers:
    res = parse_csv(
        "Work/Data/prices.csv",
        has_header=False,
        types=[str, float]
    )

    # dat file with spaces as delimiter:
    res = parse_csv(
        "Work/Data/portfolio.dat",
        delimiter=' '
    )
