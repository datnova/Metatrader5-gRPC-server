# shutdown()

Closes the previously established connection to the MetaTrader 5 terminal.

## Syntax

```python
shutdown()
```

## Parameters

None

## Return Value

None

## Example

```python
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed")
    quit()

# display data on connection status, server name and trading account
print(mt5.terminal_info())
# display data on MetaTrader 5 version
print(mt5.version())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [initialize()](./initialize.md)
- [login()](./login.md)
- [terminal_info()](./terminal_info.md)
- [version()](./version.md) 