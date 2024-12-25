# copy_ticks_range

Get ticks for the specified date range from the MetaTrader 5 terminal.

## Syntax

```python
copy_ticks_range(
    symbol,      # symbol name
    date_from,   # date the ticks are requested from
    date_to,     # date, up to which the ticks are requested
    flags        # combination of flags defining the type of requested ticks
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| date_from | datetime | Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| date_to | datetime | Date, up to which the ticks are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| flags | int | A flag to define the type of the requested ticks. COPY_TICKS_INFO – ticks with Bid and/or Ask changes, COPY_TICKS_TRADE – ticks with changes in Last and Volume, COPY_TICKS_ALL – all ticks. Required unnamed parameter. |

## Return Value

Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from the TICK_FLAG enumeration.

Returns None in case of an error. The info on the error can be obtained using [last_error()](./last_error.md).

## Note

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. The data obtained from MetaTrader 5 have UTC time.

### COPY_TICKS enumeration

| ID | Description |
|----|-------------|
| COPY_TICKS_ALL | all ticks |
| COPY_TICKS_INFO | ticks containing Bid and/or Ask price changes |
| COPY_TICKS_TRADE | ticks containing Last and/or Volume price changes |

### TICK_FLAG enumeration

| ID | Description |
|----|-------------|
| TICK_FLAG_BID | Bid price changed |
| TICK_FLAG_ASK | Ask price changed |
| TICK_FLAG_LAST | Last price changed |
| TICK_FLAG_VOLUME | Volume changed |
| TICK_FLAG_BUY | last Buy price changed |
| TICK_FLAG_SELL | last Sell price changed |

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
utc_to = datetime(2020, 1, 11, tzinfo=timezone)
# request AUDUSD ticks within 11.01.2020 - 11.01.2020
ticks = mt5.copy_ticks_range("AUDUSD", utc_from, utc_to, mt5.COPY_TICKS_ALL)
print("Ticks received:",len(ticks))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display data on each tick on a new line
print("Display obtained ticks 'as is'")
count = 0
for tick in ticks:
    count+=1
    print(tick)
    if count >= 10:
        break

# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))
```

## See also

[CopyRates](./copyrates.md), [copy_rates_from_pos](./copy_rates_from_pos.md), [copy_rates_range](./copy_rates_range.md), [copy_ticks_from](./copy_ticks_from.md), [copy_ticks_range](./copy_ticks_range.md) 