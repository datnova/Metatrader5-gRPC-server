# copy_rates_range

Get bars in the specified date range from the MetaTrader 5 terminal.

## Syntax

```python
copy_rates_range(
    symbol,      # financial instrument name
    timeframe,   # timeframe
    date_from,   # date the bars are requested from
    date_to      # date, up to which the bars are requested
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| timeframe | int | Timeframe the bars are requested for. Set by a value from the TIMEFRAME enumeration. Required unnamed parameter. |
| date_from | datetime | Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time >= date_from are returned. Required unnamed parameter. |
| date_to | datetime | Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time <= date_to are returned. Required unnamed parameter. |

## Return Value

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns.

Returns None in case of an error. The info on the error can be obtained using [last_error()](./last_error.md).

## Note

The function is similar to CopyRates in MQL5.

MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "Max. bars in chart" parameter.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. Data received from the MetaTrader 5 terminal has UTC time.

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

# import pytz module for working with time zone
import pytz

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
utc_to = datetime(2020, 1, 11, hour = 13, tzinfo=timezone)
# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
rates = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_M5, utc_from, utc_to)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
counter=0
for rate in rates:
    counter+=1
    if counter<=10:
        print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with data")
print(rates_frame.head(10))
```

## See also

[CopyRates](./copyrates.md), [copy_rates_from](./copy_rates_from.md), [copy_rates_from_pos](./copy_rates_from_pos.md), [copy_ticks_from](./copy_ticks_from.md), [copy_ticks_range](./copy_ticks_range.md) 