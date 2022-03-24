from pprint import pprint
from trading_platform.client import Client


def main():
	client = Client("http://127.0.0.1:8080")
	quotes = client.get_historic_quotes("2022-01-01 20:00", "aapl")
	pprint(quotes)


if __name__ == "__main__":
	main()