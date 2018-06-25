import csv
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = 'data/kdhx_spins_2013-2017.csv'


def parse_data(r):

    """
    Returns an ndarray of spins having a release year
    """

    headers = next(r)
    spins = []
    release_years = []
    song_title_idx = headers.index('song_name')
    release_year_idx = headers.index('disk_year')

    for row in r:
        song = row[song_title_idx]
        year = row[release_year_idx]
        if 2019 > int(year) > 1950:
            spins.append(song)
            release_years.append(year)

    return np.array([spins, release_years]).transpose()


if __name__ == '__main__':
    with open(DATA_FILE) as f:
        reader = csv.reader(f)
        parsed = parse_data(reader)
