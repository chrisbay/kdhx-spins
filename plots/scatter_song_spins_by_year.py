import csv
import numpy as np
import matplotlib.pyplot as plt

SONG_SPIN_TOTALS_FILE = 'data/song_spin_totals_with_year.csv'

with open(SONG_SPIN_TOTALS_FILE) as f:
    reader = csv.reader(f)
    years = []
    counts = []
    for row in reader:
        count = int(row[2])
        if count <= 50:
            years.append(int(row[1]))
            counts.append(count)
    plt.scatter(years, counts)
    plt.show()
