import pandas as pd

from kats.consts import TimeSeriesData
from kats.models.prophet import ProphetModel, ProphetParams
import matplotlib.pyplot as plt

# take `air_passengers` data as an example
air_passengers_df = pd.read_csv(
    "../data/air_passengers.csv",
    header=0,
    names=["time", "passengers"],
)

# convert to TimeSeriesData object
air_passengers_ts = TimeSeriesData(air_passengers_df)

# plotting origin data
air_passengers_ts.plot()
plt.show()

# create a model param instance
params = ProphetParams(seasonality_mode='multiplicative')  # additive mode gives worse results

# create a prophet model instance
m = ProphetModel(air_passengers_ts, params)

# fit model simply by calling m.fit()
m.fit()

# make prediction for next 30 month
fcst = m.predict(steps=30, freq="MS")

m.plot()
plt.show()
