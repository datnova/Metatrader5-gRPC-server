# symbol_info

Get data on the specified financial instrument.

## Syntax

```python
symbol_info(
    symbol      # financial instrument name
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name. Required unnamed parameter. |

## Return Value

Return info in the form of a named tuple structure (namedtuple) containing symbol properties. The tuple includes fields like:

- `custom` - Custom symbol flag
- `chart_mode` - Price type for constructing bars
- `select` - Symbol selection in Market Watch
- `visible` - Symbol visibility in Market Watch
- `session_deals` - Number of deals in the current session
- `session_buy_orders` - Number of Buy orders at the moment
- `session_sell_orders` - Number of Sell orders at the moment
- `volume` - Last deal volume
- `volumehigh` - Maximum volume for the day
- `volumelow` - Minimum volume for the day
- `time` - Time of the last quote
- `digits` - Number of decimal places
- `spread` - Spread value in points
- `spread_float` - Floating spread flag
- `trade_calc_mode` - Contract price calculation mode
- `trade_mode` - Order execution type
- `bid` - Current Bid price
- `ask` - Current Ask price
- `point` - Symbol point value
- `trade_tick_value` - Value of TRADE_TICK_VALUE
- `trade_tick_size` - Minimal price change
- `trade_contract_size` - Trade contract size
- `volume_min` - Minimal volume for a deal
- `volume_max` - Maximal volume for a deal
- `volume_step` - Minimal volume change step for deal execution
- `currency_base` - Basic currency of a symbol
- `currency_profit` - Profit currency
- `currency_margin` - Margin currency
- `description` - Symbol description
- `path` - Path in the symbol tree

Returns None in case of an error. The info on the error can be obtained using `last_error()`.

## Note

The function returns all data that can be obtained using `SymbolInfoInteger`, `SymbolInfoDouble` and `SymbolInfoString` in one call.

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

# attempt to enable the display of the EURJPY symbol in MarketWatch
selected = mt5.symbol_select("EURJPY", True)
if not selected:
    print("Failed to select EURJPY")
    mt5.shutdown()
    quit()

# display EURJPY symbol properties
symbol_info = mt5.symbol_info("EURJPY")
if symbol_info != None:
    # display the terminal data 'as is'    
    print(symbol_info)
    print("EURJPY: spread =", symbol_info.spread, "  digits =", symbol_info.digits)
    # display symbol properties as a list
    print("Show symbol_info(\"EURJPY\")._asdict():")
    symbol_info_dict = mt5.symbol_info("EURJPY")._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[symbols_total](symbols_total.md), [symbols_get](symbols_get.md), [symbol_select](symbol_select.md) 