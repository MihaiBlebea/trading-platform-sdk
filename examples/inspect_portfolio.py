from pprint import pprint
from trading_platform.client import Client
from time import sleep


def main():
	client = Client("http://127.0.0.1:8080", "")
	account = client.open_account()

	order = client.place_order("AAPL", "buy", 0, 1000)
	print("\nThis is the order:")
	pprint(order)

	sleep(60) # Wait for the order to be filled

	positions = client.get_portfolio()
	print("\nThis is a list of open positions:")
	pprint(positions)


if __name__ == "__main__":
	main()