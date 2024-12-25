# history_orders_get()

Get orders from trading history with the ability to filter by ticket or position.

## Syntax

1. Call specifying a time interval:
```python
history_orders_get(
    date_from,           # date the orders are requested from
    date_to,            # date, up to which the orders are requested
    group="GROUP"        # filter for selecting orders by symbols
)
```

2. Call specifying the order ticket:
```python
history_orders_get(
    ticket=TICKET        # order ticket
)
```

3. Call specifying the position ticket:
```python
history_orders_get(
    position=POSITION    # position ticket
)
```

## Parameters

- `date_from` [in] - Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.
- `date_to` [in] - Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.
- `group` [in] - The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only orders meeting a specified criteria for a symbol name.
- `ticket` [in] - Order ticket that should be received. Optional parameter. If not specified, the filter is not applied.
- `position` [in] - Ticket of a position (stored in ORDER_POSITION_ID) all orders should be received for. Optional parameter. If not specified, the filter is not applied.

### Group Filter Format

The `group` parameter may contain several comma-separated conditions:
- Use '*' as a mask in a condition
- Use '!' for logical negation
- Conditions are applied sequentially
- Include conditions should be specified first, followed by exclusion conditions

Example: `group="*, !EUR"` means select orders for all symbols first, then exclude ones containing "EUR" in symbol names.

## Return Value

Returns info in the form of a named tuple structure (namedtuple) containing order properties. Returns None in case of error. The error info can be obtained using [last_error()](./last_error.md).

## Note

The function allows receiving all history orders within a specified period in a single call similar to the HistoryOrdersTotal and HistoryOrderSelect tandem in MQL5.

## Example

```python
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# get orders for symbols whose names contain "GBP" within a specified interval
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
history_orders = mt5.history_orders_get(from_date, to_date, group="*GBP*")
if history_orders is None:
    print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
elif len(history_orders) > 0:
    print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date, to_date, len(history_orders)))
    # display these orders as a table using pandas.DataFrame
    df = pd.DataFrame(list(history_orders), columns=history_orders[0]._asdict().keys())
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    df['time_done'] = pd.to_datetime(df['time_done'], unit='s')
    print(df)

# get all orders related to the position #530218319
position_id = 530218319
position_history_orders = mt5.history_orders_get(position=position_id)
if position_history_orders is None:
    print("No orders with position #{}".format(position_id))
    print("error code =", mt5.last_error())
elif len(position_history_orders) > 0:
    print("Total history orders on position #{}: {}".format(position_id, len(position_history_orders)))
    # display these orders as a table using pandas.DataFrame
    df = pd.DataFrame(list(position_history_orders), columns=position_history_orders[0]._asdict().keys())
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    df['time_done'] = pd.to_datetime(df['time_done'], unit='s')
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [history_orders_total()](./history_orders_total.md)
- [history_deals_get()](./history_deals_get.md) 