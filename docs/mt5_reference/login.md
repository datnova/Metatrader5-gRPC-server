# login()

Connects to a trading account using specified parameters.

## Syntax

```python
login(
    login,                  # account number 
    password="PASSWORD",    # password
    server="SERVER",        # server name as specified in the terminal
    timeout=TIMEOUT         # timeout
)
```

## Parameters

- `login` [in] - Trading account number. Required unnamed parameter.

- `password` [in] - Trading account password. Optional named parameter. If not specified, the password saved in the terminal database is applied automatically.

- `server` [in] - Trade server name. Optional named parameter. If not specified, the last used server is applied automatically.

- `timeout` [in] - Connection timeout in milliseconds. Optional named parameter. Default value is 60000 (60 seconds). If the connection is not established within the specified time, the call is forcibly terminated and an exception is generated.

## Return Value

Returns True if the connection to the trade account was established successfully, otherwise returns False.

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

# connect to the trade account without specifying a password and a server
account = 17221085
authorized = mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
if authorized:
    print("connected to account #{}".format(account))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# now connect to another trading account specifying the password
account = 25115284
authorized = mt5.login(account, password="gqrtz0lbdm")
if authorized:
    # display trading account data 'as is'
    print(mt5.account_info())
    # display trading account data in the form of a list
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [initialize()](./initialize.md)
- [shutdown()](./shutdown.md)
- [account_info()](./account_info.md) 