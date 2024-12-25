# order_check()

Checks funds sufficiency for performing a required trading operation. The check result is returned as an MqlTradeCheckResult structure.

## Syntax

```python
order_check(
    request      # trading request structure
)
```

## Parameters

`request` [in] - MqlTradeRequest type structure describing the required trading action. Required unnamed parameter.

The trading request structure has the following fields:

| Field | Description |
|-------|-------------|
| action | Trading operation type. Can be one of the TRADE_REQUEST_ACTIONS values |
| magic | EA ID. Allows arranging analytical handling of trading orders |
| order | Order ticket. Required for modifying pending orders |
| symbol | Trading instrument name. Not required when modifying orders and closing positions |
| volume | Requested volume in lots |
| price | Price at which to execute the order |
| stoplimit | Price for pending Limit order when price reaches the 'price' value |
| sl | Stop Loss price |
| tp | Take Profit price |
| deviation | Maximum acceptable deviation from requested price (in points) |
| type | Order type. Can be one of the ORDER_TYPE values |
| type_filling | Order filling type. Can be one of the ORDER_TYPE_FILLING values |
| type_time | Order type by expiration. Can be one of the ORDER_TYPE_TIME values |
| expiration | Pending order expiration time (for TIME_SPECIFIED type orders) |
| comment | Order comment |
| position | Position ticket for position modification/closure |
| position_by | Opposite position ticket for closing by an opposite position |

### TRADE_REQUEST_ACTIONS Values

| ID | Description |
|----|-------------|
| TRADE_ACTION_DEAL | Place an order for an instant deal with the specified parameters (set a market order) |
| TRADE_ACTION_PENDING | Place an order for performing a deal at specified conditions (pending order) |
| TRADE_ACTION_SLTP | Change open position Stop Loss and Take Profit |
| TRADE_ACTION_MODIFY | Change parameters of the previously placed trading order |
| TRADE_ACTION_REMOVE | Remove previously placed pending order |
| TRADE_ACTION_CLOSE_BY | Close a position by an opposite one |

### ORDER_TYPE_FILLING Values

| ID | Description |
|----|-------------|
| ORDER_FILLING_FOK | Fill or Kill - can be executed only in the specified volume. If the necessary amount is currently unavailable, the order will not be executed |
| ORDER_FILLING_IOC | Immediate or Cancel - execute a deal with the volume available in the market within the specified volume. If the request cannot be filled completely, an order with the available volume will be executed |
| ORDER_FILLING_RETURN | This policy is used for market/limit/stop limit orders in Market or Exchange execution modes. Any unfilled volume will remain active |

### ORDER_TYPE_TIME Values

| ID | Description |
|----|-------------|
| ORDER_TIME_GTC | Good Till Cancelled - order stays in the queue until manually cancelled |
| ORDER_TIME_DAY | Good Till Day - order is active only during the current trading day |
| ORDER_TIME_SPECIFIED | Good Till Specified - order is active until the specified date |
| ORDER_TIME_SPECIFIED_DAY | Good Till Specified Day - order is active until 23:59:59 of the specified day |

## Return Value

Returns the result as an MqlTradeCheckResult structure containing:
- retcode: Operation return code
- balance: Balance value after the execution of the deal
- equity: Equity value after the execution of the deal
- profit: Floating profit value
- margin: Margin requirements for the deal
- margin_free: Free margin remaining after the execution of the deal
- margin_level: Margin level after the execution of the deal
- comment: Comment on the check result
- request: The structure of the trading request passed to order_check()

Returns None in case of error. The error info can be obtained using [last_error()](./last_error.md).

## Note

Successful check of a request **does not guarantee that the requested trading operation will be executed successfully**. The order_check() function is similar to OrderCheck in MQL5.

## Example

```python
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# get account currency
account_currency=mt5.account_info().currency
print("Account currency:", account_currency)

# prepare the request
symbol="USDJPY"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()

# if the symbol is unavailable in MarketWatch, add it
if not symbol_info.visible:
    print(symbol, "is not visible, trying to switch on")
    if not mt5.symbol_select(symbol, True):
        print("symbol_select({}) failed, exit".format(symbol))
        mt5.shutdown()
        quit()

# prepare the request
point = mt5.symbol_info(symbol).point
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 1.0,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "sl": mt5.symbol_info_tick(symbol).ask-100*point,
    "tp": mt5.symbol_info_tick(symbol).ask+100*point,
    "deviation": 10,
    "magic": 234000,
    "comment": "python script",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}

# perform the check and display the result 'as is'
result = mt5.order_check(request)
print(result);

# request the result as a dictionary and display it element by element
result_dict=result._asdict()
for field in result_dict.keys():
    print("   {}={}".format(field,result_dict[field]))
    # if this is a trading request structure, display it element by element as well
    if field=="request":
        traderequest_dict=result_dict[field]._asdict()
        for tradereq_filed in traderequest_dict:
            print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [order_send()](./order_send.md)
- [order_calc_margin()](./order_calc_margin.md)
- [order_calc_profit()](./order_calc_profit.md)
- [positions_get()](./positions_get.md) 