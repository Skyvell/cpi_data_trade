from pybit import usdt_perpetual, exceptions
import settings


session = usdt_perpetual.HTTP(
    endpoint = settings.BYBIT_API_ENDPOINT,
    api_key = settings.BYBIT_API_KEY,
    api_secret = settings.BYBIT_API_SECRET
)

def set_leverage_for_pair(
    symbol: str, 
    buy_leverage: int = 1, 
    sell_leverage: int = 1
    ) -> dict:

    result = session.set_leverage(
        symbol = symbol,
        buy_leverage = buy_leverage,
        sell_leverage = sell_leverage
    )

    return result

def set_cross_or_isolated(
    symbol: str, 
    is_isolated: bool = True, 
    buy_leverage: int = 1, 
    sell_leverage: int = 1
    ) -> dict:

    result = session.cross_isolated_margin_switch(
        symbol="BTCUSDT",
        is_isolated=True,
        buy_leverage=buy_leverage,
        sell_leverage=sell_leverage
    )

    return result

def place_market_order(
    symbol: str, 
    side: str, 
    quantity: int,
    leverage: int = 1,
    time_in_force: str = "GoodTillCancel",
    reduce_only: bool = False,
    close_on_trigger: bool = False,
    take_profit: int = None,
    stop_loss: int = None,
    isolated: bool = True
    ) -> dict:

    # Try switching to isolated/cross. Will raise InvalidRequestError if already set to desired type.
    # Leverage will not changed if error us raised. Thus setting leverage below. 
    try:
        set_cross_or_isolated(symbol, is_isolated=isolated, buy_leverage=leverage, sell_leverage=leverage)
    except exceptions.InvalidRequestError as e:
        print(f"set_cross_or_isolated: {e.message}.")

    # Set leverage. Will raise InvalidRequestError if leverage already set to desired leverage.
    try:
        set_leverage_for_pair(symbol, buy_leverage=leverage, sell_leverage=leverage)
    except exceptions.InvalidRequestError as e:
        print(f"set_leverage_for_pair: {e.message}.")
    
    # Open position.
    result = session.place_active_order(
        symbol = symbol,
        side = side,
        qty = quantity,
        order_type = "Market",
        time_in_force = time_in_force,
        reduce_only = reduce_only,
        close_on_trigger = close_on_trigger,
        take_profit = take_profit,
        stop_loss = stop_loss
    )

    return result