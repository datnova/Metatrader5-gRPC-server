# history_orders_total()

Get the number of orders in trading history within the specified interval.

## Syntax

```python
history_orders_total(
    date_from,           # date the orders are requested from
    date_to             # date, up to which the orders are requested
)
```

## Parameters

- `date_from` [in] - Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
- `date_to` [in] - Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

## Return Value

Returns an integer value representing the total number of orders in the specified period.

## Note

The function is similar to HistoryOrdersTotal in MQL5.

## Example

```python
from datetime import datetime
import MetaTrader5 as mt5

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# get the number of orders in history
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
history_orders = mt5.history_orders_total(from_date, to_date)
if history_orders > 0:
    print("Total history orders =", history_orders)
else:
    print("Orders not found in history")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [history_orders_get()](./history_orders_get.md) 