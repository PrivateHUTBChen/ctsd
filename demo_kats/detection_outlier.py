import pandas as pd

from kats.consts import TimeSeriesData
from kats.detectors.outlier import OutlierDetector
import matplotlib.pyplot as plt

air_passengers_outlier_df = pd.read_csv(
    "../data/air_passengers.csv",
    header=0,
    names=["time", "passengers"]
)
# manually add outlier on the date of '1950-12-01'
air_passengers_outlier_df.loc[air_passengers_outlier_df.time == '1950-12-01', 'passengers'] *= 5
# manually add outlier on the date of '1959-12-01'
air_passengers_outlier_df.loc[air_passengers_outlier_df.time == '1959-12-01', 'passengers'] *= 4

# transform the outlier data into `TimeSeriesData` Object
air_passengers_outlier_ts = TimeSeriesData(air_passengers_outlier_df)

# visualize the raw data
air_passengers_outlier_df.plot(x='time', y='passengers', figsize=(15, 8))
plt.show()

# call OutlierDetection
ts_outlierDetection = OutlierDetector(air_passengers_outlier_ts, 'additive')
# apply OutlierDetection
ts_outlierDetection.detector()

# the outliers that Outlier found
print(ts_outlierDetection.outliers[0])

# no interpolation: outlier data points will be replaced with NaN values
air_passengers_ts_outliers_removed = ts_outlierDetection.remover(interpolate=False)
# with interpolation: outlier data points will be replaced with linear interpolation values
air_passengers_ts_outliers_interpolated = ts_outlierDetection.remover(interpolate=True)

fig, ax = plt.subplots(figsize=(20, 8), nrows=1, ncols=2)

# visualize the difference between these two approaches to removing outliers
air_passengers_ts_outliers_removed.to_dataframe().plot(x='time', y='y_0', ax=ax[0])
ax[0].set_title("Outliers Removed : no interpolation")
air_passengers_ts_outliers_interpolated.to_dataframe().plot(x='time', y='y_0', ax=ax[1])
ax[1].set_title("Outliers Removed : with interpolation")
plt.show()
