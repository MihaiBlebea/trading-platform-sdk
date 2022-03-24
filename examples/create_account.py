from pprint import pprint
from trading_platform.client import Client


def main():
	client = Client("http://127.0.0.1:8080")
	account = client.open_account()
	pprint(account)

	same_account = client.get_account()
	pprint(same_account)

if __name__ == "__main__":
	main()