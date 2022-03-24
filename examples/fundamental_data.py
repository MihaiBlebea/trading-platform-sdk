from pprint import pprint
from trading_platform.client import Client


def main():
	client = Client("http://127.0.0.1:8080")
	statements = client.get_income_statement_history_quarterly("aapl")
	pprint(statements)


if __name__ == "__main__":
	main()