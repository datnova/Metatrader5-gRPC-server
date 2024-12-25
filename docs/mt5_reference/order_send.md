# order_send()

Sends a trading request to perform a trading operation from the terminal to the trade server.

## Syntax

```python
order_send(
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

## Return Value

Returns the result as an MqlTradeResult structure containing:
- retcode: Operation return code
- deal: Deal ticket if executed
- order: Order ticket
- volume: Deal volume confirmed by broker
- price: Deal price confirmed by broker
- bid: Current bid price
- ask: Current ask price
- comment: Broker comment on operation
- request_id: Request ID set by terminal during dispatch
- retcode_external: Return code of external trading system
- request: The structure of the trading request passed to order_send()

Returns None in case of error. The error info can be obtained using [last_error()](./last_error.md).

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

# prepare the buy request structure
symbol = "USDJPY"
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

lot = 0.1
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 20
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - 100 * point,
    "tp": price + 100 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}

# send a trading request
result = mt5.order_send(request)

# check the execution result
print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode={}".format(result.retcode))
    # request the result as a dictionary and display it element by element
    result_dict = result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field, result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field=="request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    print("shutdown() and quit")
    mt5.shutdown()
    quit()

print("2. order_send done, ", result)
print("   opened position with POSITION_TICKET={}".format(result.order))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [order_check()](./order_check.md)
- [positions_get()](./positions_get.md)
- [history_orders_get()](./history_orders_get.md)
- [history_deals_get()](./history_deals_get.md) 