# initialize()

Establishes a connection with the MetaTrader 5 terminal.

## Syntax

There are three ways to call this function:

1. Without parameters (auto-detect terminal):
```python
initialize()
```

2. With path to terminal:
```python
initialize(
    path                    # path to the MetaTrader 5 terminal EXE file
)
```

3. With full connection parameters:
```python
initialize(
    path,                   # path to the MetaTrader 5 terminal EXE file
    login=LOGIN,            # account number
    password="PASSWORD",    # password
    server="SERVER",        # server name as specified in the terminal
    timeout=TIMEOUT,        # timeout in milliseconds
    portable=False          # portable mode flag
)
```

## Parameters

- `path` [in] - Path to the metatrader.exe or metatrader64.exe file. Optional unnamed parameter. If not specified, the module attempts to find the executable file automatically.

- `login` [in] - Trading account number. Optional named parameter. If not specified, the last trading account is used.

- `password` [in] - Trading account password. Optional named parameter. If not specified, the password for the specified trading account saved in the terminal database is applied automatically.

- `server` [in] - Trade server name. Optional named parameter. If not specified, the server for the specified trading account saved in the terminal database is applied automatically.

- `timeout` [in] - Connection timeout in milliseconds. Optional named parameter. Default value is 60000 (60 seconds).

- `portable` [in] - Flag for launching the terminal in portable mode. Optional named parameter. Default value is False.

## Return Value

Returns True if the connection to the MetaTrader 5 terminal was established successfully, otherwise returns False.

## Notes

- If required, the MetaTrader 5 terminal is launched automatically when executing initialize().
- The terminal will be launched in portable mode if the portable parameter is set to True.

## Example

```python
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize(login=25115284, server="MetaQuotes-Demo", password="4zatlbqx"):
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# display connection status and MetaTrader 5 version
print(mt5.terminal_info())
print(mt5.version())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [shutdown()](./shutdown.md)
- [terminal_info()](./terminal_info.md)
- [version()](./version.md) 