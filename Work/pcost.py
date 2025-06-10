# pcost.py
#
# Exercise 1.27

WORK: str = os.getcwd()
CSVFILE: str = WORK + '\\Work\\Data\\portfolio.csv'

with open(CSVFILE, encoding='utf-8') as csvfile:
    data_string: str = csvfile.read()

data_lines = data_string.split('\n')
column_titles = tuple(data_lines[0].split(','))
records: list[tuple[str, int, float]] = []
for line in data_lines[1:]:
    record_items = line.split(',')
    if len(record_items) == 3:
        name: str = record_items[0]
        shares = int(record_items[1])
        price = float(record_items[2])
        records.append((name, shares, price))

for record in records:
    n, s, p = record
    print(f"{n}\t {s:>3}\t ${p:.2f}\t")
