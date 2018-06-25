import csv
import numpy as np
import matplotlib.pyplot as plt

IN_FILE = '../data/kdhx_spins_2013-2017.csv'
OUT_FILE = '../data/song_spin_totals_with_year.csv'

with open(IN_FILE) as f:
    reader = csv.reader(f)
    headers = next(reader)
    spins = []
    release_years = []
    song_title_idx = headers.index('song_name')
    release_year_idx = headers.index('disk_year')

    for row in reader:
        song = row[song_title_idx]
        year = row[release_year_idx]
        if 2019 > int(year) > 0:
            spins.append(song)
            release_years.append(year)

parsed = np.array([spins, release_years]).transpose()

years = parsed[:, 1].astype(int)
songs = parsed[:, 0].tolist()
unique_songs = list(set(songs))

with open(OUT_FILE, 'w') as out:
    out_writer = csv.writer(out, quoting=csv.QUOTE_ALL)
    for song in unique_songs:
        # TODO - overcounts if multiple songs have the same title
        play_count = songs.count(song)
        song_year = years[songs.index(song)]
        out_writer.writerow([song, song_year, play_count])
