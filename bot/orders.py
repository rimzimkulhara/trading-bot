import logging
from binance.exceptions import BinanceAPIException

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        else:
            raise ValueError("Unsupported order type")

        logging.info(f"Order success: {order}")
        return order

    except BinanceAPIException as e:
        logging.error(f"API Error: {e}")
        raise

    except Exception as e:
        logging.error(f"Error: {e}")
        raise
