# account_info()

Get info on the current trading account.

## Syntax

```python
account_info()
```

## Return Value

Return info in the form of a named tuple structure (namedtuple) containing:

| Field | Type | Description |
|-------|------|-------------|
| login | int | Account number |
| trade_mode | int | Account trade mode |
| leverage | int | Account leverage |
| limit_orders | int | Maximum allowed number of active pending orders |
| margin_so_mode | int | Mode for setting the minimal allowed margin |
| trade_allowed | bool | Permission to trade for the current account |
| trade_expert | bool | Permission to trade for an Expert Advisor |
| margin_mode | int | Margin calculation mode |
| currency_digits | int | The number of decimal places in the account currency |
| fifo_close | bool | Flag indicating that positions can only be closed by FIFO rule |
| balance | float | Account balance in the deposit currency |
| credit | float | Credit in the deposit currency |
| profit | float | Current profit in the deposit currency |
| equity | float | Account equity in the deposit currency |
| margin | float | Account margin used in the deposit currency |
| margin_free | float | Free margin of account in the deposit currency |
| margin_level | float | Account margin level in percents |
| margin_so_call | float | Margin call level |
| margin_so_so | float | Margin stop out level |
| margin_initial | float | Initial margin |
| margin_maintenance | float | Maintenance margin |
| assets | float | Current assets of account |
| liabilities | float | Current liabilities of account |
| commission_blocked | float | Current blocked commission amount |
| name | str | Client name |
| server | str | Trade server name |
| currency | str | Account currency |
| company | str | Name of a company that serves the account |

Returns None in case of an error. The error info can be obtained using [last_error()](./last_error.md).

## Note

The function returns all data that can be obtained using AccountInfoInteger, AccountInfoDouble and AccountInfoString in one call.

## Example

```python
import MetaTrader5 as mt5
import pandas as pd

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# connect to the trade account specifying a password and a server
authorized=mt5.login(25115284, password="gqz0343lbdm")
if authorized:
    account_info=mt5.account_info()
    if account_info!=None:
        # display trading account data 'as is'
        print(account_info)
        # display trading account data in the form of a dictionary
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
        print()

        # convert the dictionary into DataFrame and print
        df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
        print("account_info() as dataframe:")
        print(df)
else:
    print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [initialize()](./initialize.md)
- [shutdown()](./shutdown.md)
- [login()](./login.md) 