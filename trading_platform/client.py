from __future__ import annotations
import requests
from enum import Enum
from datetime import datetime
import json

from trading_platform.order import Order
from trading_platform.account import Account


class Direction(Enum):
	BUY = "buy"
	SELL = "sell"


class Client:

	def __init__(self, base_url: str, api_token: str, api_version: str = "v1") -> None:
		self.base_url = base_url
		self.api_token = api_token
		self.api_version = api_version

	def place_order(self, symbol: str, direction: str, quantity: int, amount: float)-> Order:
		headers = {
			"Authorization": f"Bearer {self.api_token}"
		}

		direction = Direction(direction.lower())

		payload = {
			"symbol": symbol.upper(),
			"amount": float(amount),
			"type": "limit",
			"direction": str(direction.value),
			"quantity": quantity
		}

		res = requests.post(
			f"{self.base_url}/api/{self.api_version}/order",
			json=payload,
			headers=headers,
		)

		body = res.json()

		print(body)
		if body["success"] == False:
			msg = body["error"]
			raise Exception(f"Request error: {msg}")

		order = body["order"]

		return Order(
			order["id"],
			order["symbol"],
			order["status"],
			order["direction"],
			order["amount"],
			order["fill_price"],
			order["amount_after_fill"],
			order["quantity"],
			order["filled_at"] if "filled_at" in order else None,
			order["cancelled_at"] if "cancelled_at" in order else None,
			order["created_at"],
		)

	def open_account(self)-> Account:
		res = requests.post(f"{self.base_url}/api/{self.api_version}/account")

		if res.status_code != 200:
			raise Exception(f"Status code {res.status_code}")

		body = res.json()

		if body["success"] == False:
			msg = body["error"]
			raise Exception(f"Request error: {msg}")

		account = body["account"]

		return Account(
			account["api_token"],
			account["balance"],
			account["pending_balance"],
			account["created_at"]
		)
