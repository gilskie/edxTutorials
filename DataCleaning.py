import pandas as pd
import numpy as np


def fix_zip_code(input_zip):
    try:
        input_zip = int(float(input_zip))
    except:
        try:
            input_zip = int(input_zip.split('-')[0])
        except:
            return np.NaN
    if input_zip < 10000 or input_zip > 19999:
        return np.NaN
    return str(input_zip)


def main():
    data_file = 'nyc_311_data_subset-2.csv'
    panda_data = pd.read_csv(data_file, index_col='Unique Key')

    # print(f"{panda_data}")
    # print(f"{panda_data.info()}")

    # print(f"{panda_data.iloc[1:10]}")

    # print(f"{panda_data['Incident Zip'].unique()}")

    # fixed_zip_code = fix_zip_code('UNKNOWN')
    # print(f"{fixed_zip_code}, {type(fixed_zip_code)}")

    panda_data['Incident Zip'] = panda_data['Incident Zip'].apply(fix_zip_code)
    # print(f"new incident zip: {panda_data['Incident Zip']}")
    # printing unique data from incident zip
    # panda_data['Incident Zip'] = panda_data['Incident Zip'].unique()
    # print(f"new unique value: {panda_data['Incident Zip'].unique()}")

    # remove rows that are null when displaying
    panda_data['Incident Zip'] = panda_data['Incident Zip'].notnull()

    # getting rid of null values on longitude and latitude
    panda_data = panda_data[(panda_data['Latitude'].notnull())
                            & (panda_data['Longitude'].notnull())
                            & (panda_data['Closed Date'].notnull())]

    print(f"{panda_data['Borough'].unique()}")
    # print(f"{panda_data}")
    # print(f"{panda_data.info()}")


main()
