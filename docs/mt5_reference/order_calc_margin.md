# order_calc_margin

Return margin in the account currency to perform a specified trading operation.

## Syntax

```python
order_calc_margin(
    action,      # order type (ORDER_TYPE_BUY or ORDER_TYPE_SELL)
    symbol,      # symbol name
    volume,      # volume
    price        # open price
)
```

## Parameters

- `action` (ORDER_TYPE)
  - Order type taking values from the ORDER_TYPE enumeration. Required unnamed parameter.

- `symbol` (str)
  - Financial instrument name. Required unnamed parameter.

- `volume` (float)
  - Trading operation volume. Required unnamed parameter.

- `price` (float)
  - Open price. Required unnamed parameter.

## Return Value

Real value if successful, otherwise None. The error info can be obtained using `last_error()`.

## Notes

The function allows estimating the margin necessary for a specified order type on the current account and in the current market environment without considering the current pending orders and open positions. The function is similar to OrderCalcMargin.

## ORDER_TYPE Enumeration

- `ORDER_TYPE_BUY` - Market buy order
- `ORDER_TYPE_SELL` - Market sell order
- `ORDER_TYPE_BUY_LIMIT` - Buy Limit pending order
- `ORDER_TYPE_SELL_LIMIT` - Sell Limit pending order
- `ORDER_TYPE_BUY_STOP` - Buy Stop pending order
- `ORDER_TYPE_SELL_STOP` - Sell Stop pending order
- `ORDER_TYPE_BUY_STOP_LIMIT` - Upon reaching the order price, Buy Limit pending order is placed at StopLimit price
- `ORDER_TYPE_SELL_STOP_LIMIT` - Upon reaching the order price, Sell Limit pending order is placed at StopLimit price
- `ORDER_TYPE_CLOSE_BY` - Order for closing a position by an opposite one

## Example

```python
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# get account currency
account_currency=mt5.account_info().currency
print("Account currency:",account_currency)
 
# arrange the symbol list
symbols=("EURUSD","GBPUSD","USDJPY", "USDCHF","EURJPY","GBPJPY")
print("Symbols to check margin:", symbols)
action=mt5.ORDER_TYPE_BUY
lot=0.1
for symbol in symbols:
    symbol_info=mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol,"not found, skipped")
        continue
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, skipped",symbol)
            continue
    ask=mt5.symbol_info_tick(symbol).ask
    margin=mt5.order_calc_margin(action,symbol,lot,ask)
    if margin != None:
        print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));
    else:
        print("order_calc_margin failed: , error code = ", mt5.last_error())
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [order_calc_profit](order_calc_profit.md)
- [order_check](order_check.md) 