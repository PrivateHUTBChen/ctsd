import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore')
sys.path.append("../")

from kats.consts import TimeSeriesData
from kats.models.sarima import SARIMAModel, SARIMAParams
from kats.models.prophet import ProphetModel, ProphetParams
from kats.models.holtwinters import HoltWintersModel, HoltWintersParams

data_df = pd.read_csv("../data/air_passengers.csv")
data_df.columns = ["time", "value"]
data_ts = TimeSeriesData(data_df)

# 利用SARIMA模型预测
sarima_params = SARIMAParams(
    p=2,
    d=1,
    q=1,
    trend='ct',
    seasonal_order=(1, 0, 1, 12)
)
sm = SARIMAModel(data=data_ts, params=sarima_params)
sm.fit()
sm_fcst = sm.predict(
    steps=30,
    freq="MS",
    include_history=True
)
sm.plot().set_title("SARIMA")
plt.show()

# 利用Prophet模型预测
prophet_params = ProphetParams(seasonality_mode='multiplicative')
pm = ProphetModel(data_ts, prophet_params)
pm.fit()
pm_fcst = pm.predict(
    steps=30,
    freq="MS"
)
pm.plot().set_title("Prophet")
plt.show()

# 利用Holt-Winters模型预测
