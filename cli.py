import click
from bot.client import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

setup_logger()

@click.command()
@click.option("--symbol", required=True)
@click.option("--side", required=True)
@click.option("--order_type", required=True)
@click.option("--quantity", required=True, type=float)
@click.option("--price", required=False, type=float)

def main(symbol, side, order_type, quantity, price):
    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_price(order_type, price)

        client = get_client()

        print("\n--- ORDER SUMMARY ---")
        print(symbol, side, order_type, quantity, price)

        order = place_order(client, symbol, side, order_type, quantity, price)

        print("\n--- RESPONSE ---")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

        print("\n✅ Success")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
