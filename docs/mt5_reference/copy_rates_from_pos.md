# copy_rates_from_pos

Get bars from the MetaTrader 5 terminal starting from the specified index.

## Syntax

```python
copy_rates_from_pos(
    symbol,      # financial instrument name
    timeframe,   # timeframe
    start_pos,   # initial bar index
    count        # number of bars
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| timeframe | int | Timeframe the bars are requested for. Set by a value from the TIMEFRAME enumeration. Required unnamed parameter. |
| start_pos | int | Initial index of the bar the data are requested from. The numbering of bars goes from present to past. Thus, the zero bar means the current one. Required unnamed parameter. |
| count | int | Number of bars to receive. Required unnamed parameter. |

## Return Value

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns.

Returns None in case of an error. The info on the error can be obtained using [last_error()](./last_error.md).

## Note

The function is similar to CopyRates in MQL5.

MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "Max. bars in chart" parameter.

## Example

```python
from datetime import datetime
import MetaTrader5 as mt5
import time

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# get 10 GBPUSD D1 bars from the current day
rates = mt5.copy_rates_from_pos("GBPUSD", mt5.TIMEFRAME_D1, 0, 10)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
    print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with data")
print(rates_frame)
```

## See also

[CopyRates](./copyrates.md), [copy_rates_from](./copy_rates_from.md), [copy_rates_range](./copy_rates_range.md), [copy_ticks_from](./copy_ticks_from.md), [copy_ticks_range](./copy_ticks_range.md) 