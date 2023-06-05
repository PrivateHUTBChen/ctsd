# 导入所需的包
import sys

import matplotlib.pyplot as plt
import pandas as pd
import warnings

sys.path.append("../")

warnings.filterwarnings('ignore')

# 导入单变量数据，一定要包含时间列“time”， 或者给原始数据的列重命名为“time”，
air_passengers_df = pd.read_csv(r"D:\Downloads\BrowserDownloads\kats-0.2.0\kats\data\\air_passengers.csv")

air_passengers_df.columns = ['time', 'value']

air_passengers_df.plot()
print(air_passengers_df.head(3))
print(air_passengers_df.describe())

plt.show()
