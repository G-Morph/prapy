''' a small example of fun fucking aroud with csv files '''

import csv

def extract_columns(filepath: str) -> list[dict[str, str]]:
    ''' find the desired columns in a csv file '''
    with open(filepath, 'rt', encoding='utf-8') as f:
        rows = csv.reader(f)  # get each row of data
        headers = next(rows)  # get the fist row, which contains header strings
        select = ['name', 'shares', 'price']  # the columns you want
        # where to find the columns you want:
        indices = [ headers.index(col_name) for col_name in select ]
        portfolio = [  # list comp
            { col_name: row[index] for col_name, index in zip(select, indices) }  # dict comp
            for row in rows ]
        return portfolio


if __name__ == "__main__":
    what_you_want = extract_columns('Work/Data/portfoliodate.csv')
    for thing in what_you_want:
        print(thing)
