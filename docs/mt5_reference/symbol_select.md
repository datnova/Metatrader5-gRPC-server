# symbol_select

Select a symbol in the MarketWatch window or remove a symbol from the window.

## Syntax

```python
symbol_select(
    symbol,      # financial instrument name
    enable=None  # enable or disable
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name. Required unnamed parameter. |
| enable | bool | Optional unnamed parameter. If 'false', a symbol should be removed from the MarketWatch window. Otherwise, it should be selected in the MarketWatch window. A symbol cannot be removed if open charts with this symbol are currently present or positions are opened on it. |

## Return Value

Returns True if successful, otherwise – False.

## Note

The function is similar to `SymbolSelect` in MQL5.

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

# attempt to enable the display of the EURCAD in MarketWatch
selected = mt5.symbol_select("EURCAD", True)
if not selected:
    print("Failed to select EURCAD, error code =", mt5.last_error())
else:
    symbol_info = mt5.symbol_info("EURCAD")
    print(symbol_info)
    print("EURCAD: currency_base =", symbol_info.currency_base, "  currency_profit =", symbol_info.currency_profit, "  currency_margin =", symbol_info.currency_margin)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[symbol_info](symbol_info.md), [symbols_get](symbols_get.md) 