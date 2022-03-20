from pprint import pprint
from trading_platform.client import Client


def main():
	client = Client("http://127.0.0.1:8080", "")
	account = client.open_account()

	client.api_token = account.api_token
	order = client.place_order("AAPL", "buy", 0, 1000)

	pprint(order)

if __name__ == "__main__":
	main()