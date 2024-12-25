# symbols_total

Get the number of all financial instruments in the MetaTrader 5 terminal.

## Syntax

```python
symbols_total()
```

## Return Value

Integer value representing the total number of financial instruments.

Returns None in case of an error. The info on the error can be obtained using `last_error()`.

## Note

The function returns the number of all symbols including custom ones and the ones disabled in MarketWatch.

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

# get the number of financial instruments
symbols = mt5.symbols_total()
if symbols > 0:
    print("Total symbols =", symbols)
else:
    print("symbols not found")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[symbols_get](symbols_get.md), [symbol_select](symbol_select.md), [symbol_info](symbol_info.md) 