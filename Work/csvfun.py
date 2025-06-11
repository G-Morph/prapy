''' a small example of fun fucking aroud with csv files '''

import csv


with open('Work/Data/portfolio.csv', 'rt', encoding='utf-8') as f:
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
