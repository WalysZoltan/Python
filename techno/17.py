#datetime manipulating
from datetime import datetime

a = [
    datetime(2010, 1, 1, 13, 0, 0),
    datetime(2010, 1, 1, 13, 2, 0),
    datetime(2010, 1, 1, 13, 4, 0),
    datetime(2010, 1, 1, 13, 6, 0),
    datetime(2010, 1, 1, 13, 8, 0),
    datetime(2010, 1, 1, 13, 10, 0),
    datetime(2010, 1, 1, 13, 12, 0),
]
print(int((a[5] - a[2]).total_seconds()))
