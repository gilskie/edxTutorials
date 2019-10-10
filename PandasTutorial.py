import pandas as pd
import html5lib
from pandas_datareader import data
import numpy as np
import matplotlib.pyplot as plt
import datetime

# pd.DataFrame([[[1,2,3], [1,2,3]], columns=['A', 'B', 'C']])
# print(f"{pd.DataFrame([[1, 2, 3],[1, 2, 3]], columns=['A', 'B', 'C'])}")

# data_frame = pd.DataFrame([['r1', '00', '01', '02'],
#                            ['r2', '10', '11', '12'],
#                            ['r3', '20', '21', '22']], columns=['row_label', 'A', 'B', 'C'])

# print(id(data_frame))
# data_frame.set_index('row_label', inplace=True)
# print(f"print all data frame: \r\n{data_frame}")
# print(f"get column b values only: \r\n{data_frame['B']}")

# print(f"{data_frame[['B', 'A']]}")
# print(f"{data_frame['B']}")
# print(f"describe: \r\n{data_frame.describe()}")

# transposing of data!
# print(f"transposing data: \r\n{data_frame.t}")

# selection!
# print(f"transposing data: \r\n{data_frame['A']}")

# slicing of rows!
# print(f"slicing of data: \r\n{data_frame[0:3]}")

# slicing of rows!
# print(f"slicing of data: \r\n{data_frame.loc[0]}")

# series = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(series)

# dates = pd.date_range('20191008', periods=6)
# print(dates)

# date_frames = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))
# print(date_frames)

data_frames_2 = pd.DataFrame({'A' : 1.,
                              'B' : pd.Timestamp('20191008'),
                              'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                              'D' : np.array([3] * 4, dtype='int32'),
                              'E' : pd.Categorical(["test", "train", "test", "train"]),
                              'F' : 'foo'})

# print(data_frames_2.sort_index(axis=1, ascending=True))
# print(data_frames_2.iloc[0])
# print(data_frames_2.dtypes)

# print(data_frames_2.sort_values(by='E'))
# print(data_frames_2.loc[:, ['A', 'B']])
# print(data_frames_2.describe())

print(data_frames_2['A'].sum()/data_frames_2['A'].count() * 10)

# pandas html data reader!

# data_link = 'https://www.bloomberg.com/markets/currencies'
# data_file_list = pd.read_html(data_link)
#
# print(data_file_list)