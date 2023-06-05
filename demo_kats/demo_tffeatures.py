# Initiate feature extraction class
import pandas as pd
from kats.consts import TimeSeriesData
from kats.tsfeatures.tsfeatures import TsFeatures

# take `air_passengers` data as an example
air_passengers_df = pd.read_csv(
    r"D:\Downloads\BrowserDownloads\kats-0.2.0\kats\data\\air_passengers.csv",
    header=0,
    names=["time", "passengers"],
)

# convert to TimeSeriesData object
air_passengers_ts = TimeSeriesData(air_passengers_df)

# calculate the TsFeatures
features = TsFeatures().transform(air_passengers_ts)