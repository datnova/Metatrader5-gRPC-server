# terminal_info

Get the connected MetaTrader 5 client terminal status and settings.

## Syntax

```python
terminal_info()
```

## Return Value

Return info in the form of a named tuple structure (namedtuple) with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| community_account | bool | Community account flag |
| community_connection | bool | Connection to MQL5.community status |
| connected | bool | Connection to a trade server status |
| dlls_allowed | bool | Permission to use DLL |
| trade_allowed | bool | Permission to trade |
| tradeapi_disabled | bool | Permission to use trading API |
| email_enabled | bool | Permission to send emails using SMTP-server and login specified in the terminal settings |
| ftp_enabled | bool | Permission to send reports using FTP-server and login specified in the terminal settings |
| notifications_enabled | bool | Permission to send notifications to smartphone |
| mqid | bool | Flag indicating presence of MetaQuotes ID data to send Push notifications |
| build | int | Client terminal build number |
| maxbars | int | Maximum bars count in charts |
| codepage | int | Code page of the language installed in the client terminal |
| ping_last | int | Last known value of ping to trade server in microseconds |
| community_balance | float | Community balance |
| retransmission | float | Connection data retransmission percentage |
| company | str | Company name |
| name | str | Terminal name |
| language | str | Language of terminal |
| path | str | Folder from which the terminal is started |
| data_path | str | Folder in which terminal data are stored |
| commondata_path | str | Common path for all terminals installed on a computer |

Returns None in case of an error. The info on the error can be obtained using `last_error()`.

## Note

The function returns all data that can be obtained using TerminalInfoInteger, TerminalInfoDouble and TerminalInfoString in one call.

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

# display info on MetaTrader 5 version
print(mt5.version())

# display info on the terminal settings and status
terminal_info = mt5.terminal_info()
if terminal_info != None:
    # display the terminal data 'as is'
    print(terminal_info)
    # display data in the form of a list
    print("Show terminal_info()._asdict():")
    terminal_info_dict = mt5.terminal_info()._asdict()
    for prop in terminal_info_dict:
        print("  {}={}".format(prop, terminal_info_dict[prop]))
    print()
    # convert the dictionary into DataFrame and print
    df = pd.DataFrame(list(terminal_info_dict.items()), columns=['property', 'value'])
    print("terminal_info() as dataframe:")
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[initialize](initialize.md), [shutdown](shutdown.md), [version](version.md) 