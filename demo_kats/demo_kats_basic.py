# 导入所需的包
import sys

import matplotlib.pyplot as plt
import pandas as pd
import warnings

sys.path.append("../")

warnings.filterwarnings('ignore')

# 导入单变量数据，一定要包含时间列“time”， 或者给原始数据的列重命名为“time”，
air_passengers_df = pd.read_csv("../data/air_passengers.csv")

air_passengers_df.columns = ["time", "value"]

air_passengers_df.plot()
print(air_passengers_df.head(3))
print(air_passengers_df.describe())
plt.xlabel("time")
plt.show()

# 导入多变量数据
multi_ts_df = pd.read_csv("../data/multi_ts.csv", index_col=0)
multi_ts_df.columns = ["time", "v1", "v2"]
multi_ts_df.head()
# 画在相同时间下的多变量时序图
multi_ts_df.plot()
plt.xlabel("time")
plt.show()
