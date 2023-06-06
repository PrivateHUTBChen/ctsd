import pandas as pd

from kats.consts import TimeSeriesData
from kats.models.theta import ThetaModel, ThetaParams
import matplotlib.pyplot as plt

# take `air_passengers` data as an example
air_passengers_df = pd.read_csv(
    "../data/air_passengers.csv",
    header=0,
    names=["time", "passengers"],
)

# convert to TimeSeriesData object
air_passengers_ts = TimeSeriesData(air_passengers_df)

# create ThetaParam with specifying seasonality param value
params = ThetaParams(m=12)

# create ThetaModel with given data and parameter class
m = ThetaModel(data=air_passengers_ts, params=params)

# call fit method to fit model
m.fit()

# call predict method to predict the next 30 steps
res = m.predict(steps=30, alpha=0.2)

# visualize the results
m.plot()
plt.show()
