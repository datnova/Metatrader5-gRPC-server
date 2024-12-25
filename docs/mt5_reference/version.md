# version()

Returns the MetaTrader 5 terminal version.

## Syntax

```python
version()
```

## Parameters

None

## Return Value

Returns the MetaTrader 5 terminal version, build and release date as a tuple of three values:

| Type | Description | Sample value |
|------|-------------|--------------|
| integer | MetaTrader 5 terminal version | 500 |
| integer | Build | 2007 |
| string | Build release date | '25 Feb 2019' |

Returns None in case of an error. The info on the error can be obtained using [last_error()](./last_error.md).

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

# display data on MetaTrader 5 version
print(mt5.version())

# display data on connection status, server name and trading account 'as is'
print(mt5.terminal_info())
print()

# get properties in the form of a dictionary
terminal_info_dict = mt5.terminal_info()._asdict()
# convert the dictionary into DataFrame and print
df = pd.DataFrame(list(terminal_info_dict.items()), columns=['property', 'value'])
print("terminal_info() as dataframe:")
print(df[:-1])

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See Also

- [initialize()](./initialize.md)
- [shutdown()](./shutdown.md)
- [terminal_info()](./terminal_info.md) 