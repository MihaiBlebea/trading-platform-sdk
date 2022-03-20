from datetime import datetime
from dataclasses import dataclass


@dataclass
class Account:

	api_token: str

	balance: float

	pending_balance: float

	created_at: datetime