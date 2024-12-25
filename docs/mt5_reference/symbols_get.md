# symbols_get

Get all financial instruments from the MetaTrader 5 terminal.

## Syntax

```python
symbols_get(
    group="GROUP"    # symbol selection filter
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| group | str | The filter for arranging a group of necessary symbols. Optional parameter. If the group is specified, the function returns only symbols meeting the specified criteria. |

## Return Value

Return symbols in the form of a tuple. Each symbol is represented as a named tuple structure containing symbol properties.

Returns None in case of an error. The info on the error can be obtained using `last_error()`.

## Note

The `group` parameter allows sorting out symbols by name. '*' can be used at the beginning and the end of a string.

The `group` parameter can be used as a named or an unnamed one. Both options work the same way. The named option (group="GROUP") makes the code easier to read.

The `group` parameter may contain several comma separated conditions. A condition can be set as a mask using '*'. The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially, which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="*, !EUR" means that all symbols should be selected first and the ones containing "EUR" in their names should be excluded afterwards.

Unlike `symbol_info()`, the `symbols_get()` function returns data on all requested symbols within a single call.

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

# get all symbols
symbols = mt5.symbols_get()
print('Symbols: ', len(symbols))
count = 0
# display the first five ones
for s in symbols:
    count += 1
    print("{}.  {}".format(count, s.name))
    if count == 5: break
print()

# get symbols containing RU in their names
ru_symbols = mt5.symbols_get("*RU*")
print('len(*RU*): ', len(ru_symbols))
for s in ru_symbols:
    print(s.name)
print()

# get symbols whose names do not contain USD, EUR, JPY and GBP
group_symbols = mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
for s in group_symbols:
    print(s.name, ":", s)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[symbols_total](symbols_total.md), [symbol_select](symbol_select.md), [symbol_info](symbol_info.md) 