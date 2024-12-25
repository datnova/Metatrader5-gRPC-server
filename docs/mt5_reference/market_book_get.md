# market_book_get

Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

## Syntax

```python
market_book_get(
    symbol      # financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name. Required unnamed parameter. |

## Return Value

Returns the Market Depth content as a tuple from BookInfo entries featuring order type, price and volume in lots. BookInfo is similar to the MqlBookInfo structure.

Returns None in case of an error. The info on the error can be obtained using [last_error](last_error.md).

## Note

The subscription to the Market Depth change events should be preliminarily performed using the [market_book_add](market_book_add.md) function.

The function is similar to MarketBookGet in MQL5.

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
    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()
    quit()

# subscribe to market depth updates for EURUSD (Depth of Market)
if mt5.market_book_add('EURUSD'):
    # get the market depth data 10 times in a loop
    for i in range(10):
        # get the market depth content (Depth of Market)
        items = mt5.market_book_get('EURUSD')
        # display the entire market depth 'as is' in a single string
        print(items)
        # now display each order separately for more clarity
        if items:
            for it in items:
                # order content
                print(it._asdict())
        # pause for 5 seconds before the next request of the market depth data
        time.sleep(5)
    # cancel the subscription to the market depth updates (Depth of Market)
    mt5.market_book_release('EURUSD')
else:
    print("mt5.market_book_add('EURUSD') failed, error code =", mt5.last_error())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[market_book_add](market_book_add.md), [market_book_release](market_book_release.md) 