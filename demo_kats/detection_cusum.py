import numpy as np
import pandas as pd
from kats.consts import TimeSeriesData, TimeSeriesIterator
from kats.detectors.cusum_detection import CUSUMDetector
import matplotlib.pyplot as plt

# synthesize data with simulation
np.random.seed(10)
df = pd.DataFrame(
    {
        'time': pd.date_range('2019-01-01', '2019-03-01'),
        'increase': np.concatenate([np.random.normal(1, 0.2, 30), np.random.normal(2, 0.2, 30)]),
        'decrease': np.concatenate([np.random.normal(1, 0.3, 50), np.random.normal(0.5, 0.3, 10)]),
    }
)

# detect increase
timeseries = TimeSeriesData(
    df.loc[:, ['time', 'increase']]
)
detector = CUSUMDetector(timeseries)
# run detector
change_points = detector.detector(change_directions=["increase"])
# plot the results
detector.plot(change_points).set_title("increase")
plt.xticks(rotation=45)
plt.show()

# detect decrease
timeseries = TimeSeriesData(
    df.loc[:, ['time', 'decrease']]
)
detector = CUSUMDetector(timeseries)
# run detector
change_points = detector.detector(change_directions=["decrease"])
# plot the results
detector.plot(change_points).set_title("decrease")
plt.xticks(rotation=45)
plt.show()

# # detect increase
# timeseries = TimeSeriesData(
#     df.loc[:, ['time', 'increase']]
# )
# detector = CUSUMDetector(timeseries)
# # run detector
# change_points = detector.detector(change_directions=["decrease"])
# # plot the results
# detector.plot(change_points)
# plt.xticks(rotation=45)
# plt.show()
#
# # detect increase
# timeseries = TimeSeriesData(
#     df.loc[:,['time','increase']]
# )
# detector = CUSUMDetector(timeseries)
# # run detector
# change_points = detector.detector()
# # plot the results
# detector.plot(change_points)
# plt.xticks(rotation=45)
# plt.show()


