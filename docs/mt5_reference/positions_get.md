# positions_get()

Get open positions with the ability to filter by symbol or ticket. There are three call options.

## Syntax

1. Call without parameters to return open positions for all symbols:
```python
positions_get()
```

2. Call specifying a symbol to get open positions for:
```python
positions_get(
    symbol="SYMBOL"      # symbol name
)
```

3. Call specifying a group of symbols to filter positions by:
```python
positions_get(
    group="GROUP"        # filter for selecting positions by symbols
)
```

4. Call specifying a position ticket:
```python
positions_get(
    ticket=TICKET        # ticket
)
```

## Parameters

- `symbol` [in] - Symbol name. Optional named parameter. If a symbol is specified, the ticket parameter is ignored.
- `group` [in] - The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only positions meeting the specified criteria for symbol names.
- `ticket` [in] - Position ticket (POSITION_TICKET). Optional named parameter.

### Group Filter Format

The `group` parameter may contain several comma-separated conditions:
- Use '*' as a mask in a condition
- Use '!' for logical negation
- Conditions are applied sequentially
- Include conditions should be specified first, followed by exclusion conditions

Example: `group="*, !EUR"` means select positions for all symbols first, then exclude ones containing "EUR" in symbol names.

## Return Value

Returns info in the form of a named tuple structure (namedtuple) containing:
- ticket: Position ticket
- time: Position opening time
- type: Position type (0 - buy, 1 - sell)
- magic: Position magic number
- identifier: Position identifier
- reason: Position opening reason
- volume: Position volume
- price_open: Position opening price
- sl: Stop Loss level
- tp: Take Profit level
- price_current: Current price
- swap: Cumulative swap
- profit: Current profit
- symbol: Position symbol
- comment: Position comment

Returns None in case of error. The error info can be obtained using [last_error()](./last_error.md).

## Note

The function allows receiving all open positions within one call similar to the PositionsTotal and PositionSelect tandem in MQL5.

## Example

```python
import MetaTrader5 as mt5
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# get open positions on USDCHF
positions = mt5.positions_get(symbol="USDCHF")
if positions is None:
    print("No positions on USDCHF, error code={}".format(mt5.last_error()))
elif len(positions) > 0:
    print("Total positions on USDCHF =", len(positions))
    # display all open positions
    for position in positions:
        print(position)

# get the list of positions on symbols whose names contain "*USD*"
usd_positions = mt5.positions_get(group="*USD*")
if usd_positions is None:
    print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(usd_positions) > 0:
    print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))
    # display these positions as a table using pandas.DataFrame
    df = pd.DataFrame(list(usd_positions), columns=usd_positions[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [positions_total()](./positions_total.md)
- [orders_get()](./orders_get.md)
- [history_orders_get()](./history_orders_get.md)
- [history_deals_get()](./history_deals_get.md) 