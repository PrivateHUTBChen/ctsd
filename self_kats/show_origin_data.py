import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv(
    # 数据地址
    "../data/air_passengers.csv",
    usecols=[0, 1]
)
print(data_df)
data_df.columns = ["time", "value"]
data_df.plot(x="time")
plt.xticks(rotation=30)
plt.show()
