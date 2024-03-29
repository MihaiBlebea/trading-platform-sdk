# Trading Platform Python SDK

This is the SDK for the Go trading platform API.

## How to install?

`pip install trading-platform` or `pip3 install trading-platform`

## How to use?

First check the examples folder to get a better understanding of how the library works.

If you don't have time for that, just read the features with code examples in here.

### 1. Open an account

This opens an account on the trading platform with a base balance of $10000 and returns an API Token that you can use to make other calls to the API.

Please store the API Token safely.

After calling the open account method, the API Token is auto-saved into the client instance, so no need to set it again.

**Example:**

```python
from pprint import pprint
from trading_platform.client import Client

def main():
	client = Client("http://127.0.0.1:8080") # you need to provide the base url of the trading platform API 
	account = client.open_account()
	pprint(account)

	same_account = client.get_account()
	pprint(same_account)

if __name__ == "__main__":
	main()
```

### 2. Place an order

You can place a buy or sell order on the trading platform.

For now, we don't support stop-loss orders or take-profit, but those will come shortly.

**Example:**

```python
from pprint import pprint
from trading_platform.client import Client

def main():
	client = Client("http://127.0.0.1:8080")
	account = client.open_account()

	order = client.place_order("AAPL", "buy", 0, 1000)
	print("\nThis is a buy order:")
	pprint(order)

	orders = client.get_orders()
	print("\nThis is a list of orders:")
	pprint(orders)


if __name__ == "__main__":
	main()
```

### 3. Inspect your portfolio

Once you place an order, it will appear as `pending` in your orders list.

The position will not be added to your portfolio, until the order is `filled`.

There is a worker that checks the bid and ask prices for the symbols and takes care of processingthe order.

Once your order has been filled, it will be shown in your portfolio as an open position.

If you partially sell the symbol it will be reflected in the portfolio.

If you completely close the position, it will be removed from your portfolio (closing a position is equivalent with selling all the quantity of the stock held).

**Example:**

```python
from pprint import pprint
from trading_platform.client import Client
from time import sleep

def main():
	client = Client("http://127.0.0.1:8080")
	client.open_account()

	order = client.place_order("AAPL", "buy", 0, 1000)
	print("\nThis is the order:")
	pprint(order)

	sleep(60) # Wait for the order to be filled

	positions = client.get_portfolio()
	print("\nThis is a list of open positions:")
	pprint(positions)

if __name__ == "__main__":
	main()
```

### 4. Get historic quote data

You can receive historic quote data for any stock supported.

For now, we just support stock shares but in the future we can add crypto, options and futures.

You need to supply a start date, the quotes will cover minute by minute the time between the start date and now.

This feature needs improving as you may need more filtering power. Soon to come.

**Example:**

```python
from pprint import pprint
from trading_platform.client import Client

def main():
	client = Client("http://127.0.0.1:8080")
	quotes = client.get_historic_quotes("2022-01-01 20:00", "aapl")
	pprint(quotes)

if __name__ == "__main__":
	main()
```


### 5. Get fundamental data

If you are planning to value trade, you need to analyse the balance sheet of the company and calculate the real company price.

To help with that, use this method to get all the fundamental data from the yahoo finance API.

Available data as of now:

- income statement history quarterly

- more to come soon...


**Example:**

```python
from pprint import pprint
from trading_platform.client import Client

def main():
	client = Client("http://127.0.0.1:8080")
	statements = client.get_income_statement_history_quarterly("aapl")
	pprint(statements)

if __name__ == "__main__":
	main()
```


### Enjoy the library and let us know if you would like to see any extra features

*Email: mihaiserban.blebea@gmail.com*
