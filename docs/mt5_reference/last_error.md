# last_error()

Returns data about the last error that occurred during the execution of MetaTrader 5 library functions.

## Syntax

```python
last_error()
```

## Parameters

None

## Return Value

Returns a tuple containing:
- Error code (integer)
- Error description (string)

## Error Codes

| Constant | Value | Description |
|----------|--------|-------------|
| RES_S_OK | 1 | Generic success |
| RES_E_FAIL | -1 | Generic fail |
| RES_E_INVALID_PARAMS | -2 | Invalid arguments/parameters |
| RES_E_NO_MEMORY | -3 | No memory condition |
| RES_E_NOT_FOUND | -4 | No history |
| RES_E_INVALID_VERSION | -5 | Invalid version |
| RES_E_AUTH_FAILED | -6 | Authorization failed |
| RES_E_UNSUPPORTED | -7 | Unsupported method |
| RES_E_AUTO_TRADING_DISABLED | -8 | Auto-trading disabled |
| RES_E_INTERNAL_FAIL | -10000 | Internal IPC general error |
| RES_E_INTERNAL_FAIL_SEND | -10001 | Internal IPC send failed |
| RES_E_INTERNAL_FAIL_RECEIVE | -10002 | Internal IPC recv failed |
| RES_E_INTERNAL_FAIL_INIT | -10003 | Internal IPC initialization fail |
| RES_E_INTERNAL_FAIL_CONNECT | -10003 | Internal IPC no ipc |
| RES_E_INTERNAL_FAIL_TIMEOUT | -10005 | Internal timeout |

## Example

```python
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code = ", mt5.last_error())
    quit()

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [version()](./version.md)
- [initialize()](./initialize.md) 