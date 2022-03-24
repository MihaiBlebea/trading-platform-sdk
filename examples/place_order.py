from pprint import pprint
from trading_platform.client import Client


def main():
	client = Client("http://127.0.0.1:8080")
	account = client.open_account()

	order = client.place_order("AAPL", "buy", 0, 1000)
	print("\nThis is the initial order:")
	pprint(order)

	orders = client.get_orders()
	print("\nThis is a list of orders:")
	pprint(orders)


if __name__ == "__main__":
	main()