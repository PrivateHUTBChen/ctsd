from kats.consts import TimeSeriesData
from kats.tsfeatures.tsfeatures import TsFeatures

import pandas as pd

# take `air_passengers` data as an example
air_passengers_df = pd.read_csv(
    "../data/air_passengers.csv",
    header=0,
    names=["time", "passengers"],
)

air_passengers_ts = TimeSeriesData(air_passengers_df)

tsFeature = TsFeatures()
features_air_passengers = TsFeatures().transform(air_passengers_ts)

print(features_air_passengers)