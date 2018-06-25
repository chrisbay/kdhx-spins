import csv
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = 'data/kdhx_spins_2013-2017.csv'

input_artist = input("Artist: ")
search_artist = input_artist.lower()

spins = []
years = []

with open(DATA_FILE) as f:
    reader = csv.reader(f)
    headers = next(reader)
    song_title_idx = headers.index('song_name')
    artist_idx = headers.index('artist_name')
    playlist_date_idx = headers.index('playlist_date')
    for row in reader:
        song = row[song_title_idx]
        artist = row[artist_idx]
        try:
            year = int(row[playlist_date_idx][-4:])
        except:
            print('Invalid year:', row[spin_year_idx][-4:])
        if search_artist in artist.lower():
            spins.append(song)
            years.append(year)

unique_years = sorted(list(set(years)))
counts = []

for year in unique_years:
    count = years.count(year)
    counts.append(count)

plt.plot(unique_years, counts)
plt.title(input_artist + ' Spins By Year on KDHX')
plt.xlabel('Year')
plt.ylabel('# of Spins')
plt.xticks(unique_years)
plt.show()
