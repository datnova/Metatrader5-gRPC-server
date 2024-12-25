# symbol_info_tick

Get the last tick for the specified financial instrument.

## Syntax

```python
symbol_info_tick(
    symbol      # financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name. Required unnamed parameter. |

## Return Value

Return info in the form of a named tuple structure (namedtuple) containing the following fields:

- `time` - Time of the last quote (in seconds)
- `bid` - Current Bid price
- `ask` - Current Ask price
- `last` - Price of the last deal (Last)
- `volume` - Volume for the current Last price
- `time_msc` - Time of the last quote in milliseconds
- `flags` - Tick flags
- `volume_real` - Volume for the current Last price with greater accuracy

Returns None in case of an error. The info on the error can be obtained using `last_error()`.

## Note

The function is similar to `SymbolInfoTick` in MQL5.

## Example

```python
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# attempt to enable the display of the GBPUSD in MarketWatch
selected = mt5.symbol_select("GBPUSD", True)
if not selected:
    print("Failed to select GBPUSD")
    mt5.shutdown()
    quit()

# display the last GBPUSD tick
lasttick = mt5.symbol_info_tick("GBPUSD")
print(lasttick)
# display tick field values in the form of a list
print("Show symbol_info_tick(\"GBPUSD\")._asdict():")
symbol_info_tick_dict = mt5.symbol_info_tick("GBPUSD")._asdict()
for prop in symbol_info_tick_dict:
    print("  {}={}".format(prop, symbol_info_tick_dict[prop]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[symbol_info](symbol_info.md), [symbol_select](symbol_select.md) 