import csv
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = 'data/kdhx_spins_2013-2017.csv'

release_years = []

with open(DATA_FILE) as f:
    reader = csv.reader(f)
    headers = next(reader)
    release_year_idx = headers.index('disk_year')

    for row in reader:
        year = row[release_year_idx]
        if 2019 > int(year) > 1950:
            release_years.append(int(year))

min_year = min(release_years)
max_year = max(release_years)
num_bins = (max_year - min_year) / 1

plt.hist(release_years, bins=int(num_bins))
plt.title('Song Spins by Release Year')
plt.xlabel('Year')
plt.ylabel('Count of Spins')
plt.show()
