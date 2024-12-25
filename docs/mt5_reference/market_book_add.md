# market_book_add

Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

## Syntax

```python
market_book_add(
    symbol      # financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name. Required unnamed parameter. |

## Return Value

Returns True if successful, otherwise – False.

## Note

The function is similar to `MarketBookAdd` in MQL5.

## Example

```python
import MetaTrader5 as mt5
import time

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# subscribe to market depth updates for EURUSD
if not mt5.market_book_add('EURUSD'):
    print("Failed to subscribe to market depth for EURUSD, error code =", mt5.last_error())
    mt5.shutdown()
    quit()

# get market depth data
depth = mt5.market_book_get('EURUSD')
if depth is None:
    print("No market depth data")
else:
    print("Market depth for EURUSD:")
    for item in depth:
        print(item)

# unsubscribe from market depth updates for EURUSD
mt5.market_book_release('EURUSD')

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[market_book_get](market_book_get.md), [market_book_release](market_book_release.md) 