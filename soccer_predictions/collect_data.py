import pandas as pd
import urllib2
import os


def clean_year_format(year):
    if type(year) is int and len(str(year)) == 1:
        corrected_year = '0{}'.format(year)
    else:
        corrected_year = year
    nb_digits = len(str(corrected_year))
    if nb_digits == 4:
        return str(corrected_year)[-2:]
    elif nb_digits == 2:
        return str(corrected_year)
    else:
        raise ValueError('year must have two (ex: 14 for 2014) or four (ex: 2014) digits')


def check_valid_start_end(start, end):
    return int(end) - int(start) == 1


def download_french_championship_results(division_index, year_start, year_end, output_filepath):
    start = clean_year_format(year_start)
    end = clean_year_format(year_end)
    if not check_valid_start_end(start, end):
        raise ValueError('year_end must be year after year_start (ex: year_start=14 and year_end=15 '
                         'to download results of 14/15 championship')
    champ = 'F{}'.format(division_index)
    url = 'http://www.football-data.co.uk/mmz4281/{}{}/{}.csv'.format(start, end, champ)
    print('Downloading ligue{} results for year {}-{}'.format(champ[-1], start, end))
    f = urllib2.urlopen(url)
    dir_path = os.path.dirname(output_filepath)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(output_filepath, "wb") as local_file:
        local_file.write(f.read())


def prepare_dataset(raw_df, inplace=True):
    if inplace:
        df = raw_df
    else:
        df = raw_df.copy()

    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
    for col in ['Bb1X2', 'BbMxH', 'BbAvH', 'BbMxD', 'BbAvD', 'BbMxA', 'BbAvA', 'BbOU', 'BbMx>2.5', 'BbAv>2.5',
                'BbMx<2.5', 'BbAv<2.5', 'BbAH', 'BbAHh', 'BbMxAHH', 'BbAvAHH', 'BbMxAHA', 'BbAvAHA',
                'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'IWH', 'IWD', 'IWA', 'LBH', 'LBD', 'LBA',
                'SJH', 'SJD', 'SJA', 'VCH', 'VCD', 'VCA', 'PSCH', 'PSCD', 'PSCA', 'PSH', 'PSD', 'PSA', 'WHH',
                'WHD', 'WHA']:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)
    if not inplace:
        return df


def main():
    years = ['2013', '2014', '2015', '2016', '2017']
    champs = [1, 2]
    base_dir = os.path.dirname(os.path.abspath('__file__'))
    output_dir = '{}/data'.format(base_dir)

    for champ in champs:
        for year in years:
            year_start = year
            year_end = str(int(year) + 1)
            filepath = '{}/results_ligue{}_{}_{}.csv'.format(output_dir, champ, year_start, year_end)
            download_french_championship_results(champ, year_start, year_end, filepath)
            raw_df = pd.read_csv(filepath)
            df = prepare_dataset(raw_df, inplace=False)
            df.to_csv(filepath, index=False)


if __name__ == '__main__':
    main()
