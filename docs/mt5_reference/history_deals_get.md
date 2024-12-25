# history_deals_get()

Get deals from trading history within the specified interval with the ability to filter by ticket or position.

## Syntax

1. Call specifying a time interval:
```python
history_deals_get(
    date_from,           # date the deals are requested from
    date_to,             # date, up to which the deals are requested
    group="GROUP"        # filter for selecting deals for symbols
)
```

2. Call specifying the order ticket:
```python
history_deals_get(
    ticket=TICKET        # order ticket
)
```

3. Call specifying the position ticket:
```python
history_deals_get(
    position=POSITION    # position ticket
)
```

## Parameters

- `date_from` [in] - Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.
- `date_to` [in] - Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.
- `group` [in] - The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only deals meeting a specified criteria for a symbol name.
- `ticket` [in] - Ticket of an order (stored in DEAL_ORDER) all deals should be received for. Optional parameter. If not specified, the filter is not applied.
- `position` [in] - Ticket of a position (stored in DEAL_POSITION_ID) all deals should be received for. Optional parameter. If not specified, the filter is not applied.

### Group Filter Format

The `group` parameter may contain several comma-separated conditions:
- Use '*' as a mask in a condition
- Use '!' for logical negation
- Conditions are applied sequentially
- Include conditions should be specified first, followed by exclusion conditions

Example: `group="*, !EUR"` means select deals for all symbols first, then exclude ones containing "EUR" in symbol names.

## Return Value

Returns info in the form of a named tuple structure (namedtuple) containing:
- ticket: Deal ticket
- order: Order ticket
- time: Deal execution time
- time_msc: Deal execution time in milliseconds
- type: Deal type
- entry: Deal entry - entry in, entry out, reverse
- magic: Expert Advisor ID
- position_id: Position identifier
- reason: Deal execution reason
- volume: Deal volume
- price: Deal price
- commission: Deal commission
- swap: Cumulative swap
- profit: Deal profit
- fee: Deal fee charged
- symbol: Deal symbol
- comment: Deal comment
- external_id: Deal identifier in an external trading system

Returns None in case of error. The error info can be obtained using [last_error()](./last_error.md).

## Note

The function allows receiving all history deals within a specified period in a single call similar to the HistoryDealsTotal and HistoryDealSelect tandem in MQL5.

## Example

```python
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# get deals for symbols whose names contain "GBP" within a specified interval
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
deals = mt5.history_deals_get(from_date, to_date, group="*GBP*")
if deals is None:
    print("No deals with group=\"*GBP*\", error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date, to_date, len(deals)))
    # display these deals as a table using pandas.DataFrame
    df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)

# get all deals related to the position #530218319
position_id = 530218319
position_deals = mt5.history_deals_get(position=position_id)
if position_deals is None:
    print("No deals with position #{}".format(position_id))
    print("error code =", mt5.last_error())
elif len(position_deals) > 0:
    print("Deals with position id #{}: {}".format(position_id, len(position_deals)))
    # display these deals as a table using pandas.DataFrame
    df = pd.DataFrame(list(position_deals), columns=position_deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [history_deals_total()](./history_deals_total.md)
- [history_orders_get()](./history_orders_get.md) 