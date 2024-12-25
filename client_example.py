from datetime import datetime, timedelta
import random

import grpc
from mt5_grpc_proto import common_pb2, common_pb2_grpc, position_pb2, deal_pb2, history_orders_pb2_grpc, position_pb2_grpc, \
    symbol_info_pb2_grpc, history_orders_pb2, terminal_pb2, symbols_pb2_grpc, order_pb2, terminal_pb2_grpc
from mt5_grpc_proto import symbol_info_pb2, deal_pb2_grpc, order_pb2_grpc, symbols_pb2

if __name__ == '__main__':
    with (grpc.insecure_channel('192.168.10.100:50051') as channel):
        # Connect to MetaTrader
        mt = common_pb2_grpc.MetaTraderServiceStub(channel)
        mt.Connect(common_pb2.Empty())

        # Get terminal info
        terminal = terminal_pb2_grpc.TerminalInfoServiceStub(channel)
        terminal_info = terminal.GetTerminalInfo(terminal_pb2.TerminalInfoRequest())
        print("Terminal Info:")
        print(terminal_info)

        # Get symbols service stub
        symbols = symbols_pb2_grpc.SymbolsServiceStub(channel)
        
        # Get list of all symbols
        symbols_list = symbols.GetSymbols(symbols_pb2.SymbolsGetRequest())
        print("Available symbols:", [symbol for symbol in symbols_list.symbols])
        
        # Select random symbol and set it as active
        if symbols_list.symbols:
            random_symbol = random.choice(symbols_list.symbols)
            select_response = symbols.SelectSymbol(symbols_pb2.SymbolSelectRequest(
                symbol=random_symbol,
                enable=True
            ))
            if select_response.success:
                print(f"Selected random symbol: {random_symbol}")
            else:
                print(f"Failed to select symbol: {select_response.error.description}")

        positions_total = position_pb2_grpc.PositionsServiceStub(channel).GetPositionsTotal(
            position_pb2.PositionsTotalRequest()
        )

        print("Total positions: ", positions_total.total)

        # Get all positions
        # Get symbol info for EURUSD
        symbol_info = symbol_info_pb2_grpc.SymbolInfoServiceStub(channel).GetSymbolInfo(symbol_info_pb2.SymbolInfoRequest(
            symbol="EURUSD"
        ))

        if symbol_info.error.code == 0:
            info = symbol_info.symbol_info
            print("\nEURUSD Symbol Details:")
            print(f"Bid: {info.bid}")
            print(f"Ask: {info.ask}")
            print(f"Point: {info.point}")
            print(f"Digits: {info.digits}")
            print(f"Spread: {info.spread}")
            print(f"Trade mode: {info.trade_mode}")
            print(f"Volume min: {info.volume_min}")
            print(f"Volume max: {info.volume_max}")
            print(f"Volume step: {info.volume_step}")
        else:
            print(f"Failed to get EURUSD info: {symbol_info.error.message}")

        # Get orders history
        orders_service = order_pb2_grpc.OrdersServiceStub(channel)
        orders = orders_service.GetOrders(order_pb2.OrdersGetRequest())
        print("\nActive Orders:")
        if orders.error.code == 0:
            for order in orders.orders:
                print(f"Order #{order.ticket}:")
                print(f"  Symbol: {order.symbol}")
                print(f"  Type: {order.type}")
                print(f"  Volume: {order.volume_current}")
                print(f"  Open Price: {order.price_open}")
                print(f"  Current Price: {order.price_current}")
                print(f"  Stop Loss: {order.stop_loss}")
                print(f"  Take Profit: {order.take_profit}")
                print(f"  Comment: {order.comment}")
        else:
            print(f"Failed to get orders: {orders.error.message}")

        # Get deals history for the last day
        trade_history = deal_pb2_grpc.TradeHistoryServiceStub(channel)
        
        # Calculate timestamps for the last 24 hours
        now = datetime.now()
        yesterday = now - timedelta(days=10)
        
        deals_request = deal_pb2.DealsRequest(
            time_filter=common_pb2.TimeFilter(
                date_from=int(yesterday.timestamp()),
                date_to=int(now.timestamp())
            )
        )
        
        deals = trade_history.GetDeals(deals_request)
        print("\nDeals History (last 24 hours):")
        if deals.error is None or deals.error.code == 0:
            for deal in deals.deals:
                print(f"Deal #{deal.ticket}:")
                print(f"  Symbol: {deal.symbol}")
                print(f"  Type: {deal.type}")
                print(f"  Entry: {deal.entry}")
                print(f"  Volume: {deal.volume}")
                print(f"  Price: {deal.price}")
                print(f"  Profit: {deal.profit}")
                print(f"  Commission: {deal.commission}")
                print(f"  Swap: {deal.swap}")
                print(f"  Comment: {deal.comment}")
        else:
            print(f"Failed to get deals history: {deals.error.message}")

        # Get orders history for the last 10 days
        history_orders_service = history_orders_pb2_grpc.HistoryOrdersServiceStub(channel)
        
        # Get total number of orders in history
        history_orders_total = history_orders_service.GetHistoryOrdersTotal(
            history_orders_pb2.HistoryOrdersTotalRequest(
                date_from=int(yesterday.timestamp()),
                date_to=int(now.timestamp())
            )
        )
        print(f"\nTotal orders in history for last 10 days: {history_orders_total.total}")
        
        # Get detailed orders history
        history_orders_request = history_orders_pb2.HistoryOrdersRequest(
            time_filter=common_pb2.TimeFilter(
                date_from=int(yesterday.timestamp()),
                date_to=int(now.timestamp())
            ),
            group="*"  # Get all symbols
        )
        
        history_orders = history_orders_service.GetHistoryOrders(history_orders_request)
        print("\nOrders History (last 10 days):")
        if history_orders.error is None or history_orders.error.code == 0:
            for order in history_orders.orders:
                print(f"Order #{order.ticket}:")
                print(f"  Symbol: {order.symbol}")
                print(f"  Type: {order.type}")
                print(f"  State: {order.state}")
                print(f"  Volume Initial: {order.volume_initial}")
                print(f"  Volume Current: {order.volume_current}")
                print(f"  Price Open: {order.price_open}")
                print(f"  Stop Loss: {order.stop_loss}")
                print(f"  Take Profit: {order.take_profit}")
                print(f"  Comment: {order.comment}")
        else:
            print(f"Failed to get orders history: {history_orders.error.message}")
        