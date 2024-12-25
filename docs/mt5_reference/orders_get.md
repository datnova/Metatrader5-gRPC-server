# orders_get

Get active orders with the ability to filter by symbol or ticket. There are three call options.

## Syntax

```python
# Get active orders on all symbols
orders_get()

# Get active orders for a specified symbol
orders_get(
    symbol="SYMBOL"      # symbol name
)

# Get active orders for a group of symbols
orders_get(
    group="GROUP"        # filter for selecting orders for symbols
)

# Get active order by ticket
orders_get(
    ticket=TICKET        # ticket
)
```

## Parameters

- `symbol` (str, optional)
  - Symbol name. If specified, the `ticket` parameter is ignored.

- `group` (str, optional)
  - Filter for arranging a group of necessary symbols. If specified, the function returns only active orders meeting the specified criteria for symbol names.
  - Can use '*' at the beginning and end of the string
  - Can contain several comma-separated conditions
  - Conditions can be set as masks using '*'
  - The logical negation symbol '!' can be used for exclusion
  - Example: `group="*, !EUR"` means select orders for all symbols first, then exclude ones containing "EUR"

- `ticket` (int, optional)
  - Order ticket (ORDER_TICKET)

## Return Value

Returns info in the form of a named tuple structure (namedtuple). Returns None in case of an error. The info on the error can be obtained using `last_error()`.

## Notes

The function allows receiving all active orders within one call similar to the OrdersTotal and OrderSelect tandem.

## Example

```python
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# display data on active orders on GBPUSD
orders=mt5.orders_get(symbol="GBPUSD")
if orders is None:
    print("No orders on GBPUSD, error code={}".format(mt5.last_error()))
else:
    print("Total orders on GBPUSD:",len(orders))
    # display all active orders
    for order in orders:
        print(order)
print()
 
# get the list of orders on symbols whose names contain "*GBP*"
gbp_orders=mt5.orders_get(group="*GBP*")
if gbp_orders is None:
    print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
else:
    print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))
    # display these orders as a table using pandas.DataFrame
    df=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    print(df)
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [orders_total](orders_total.md)
- [positions_get](positions_get.md) 