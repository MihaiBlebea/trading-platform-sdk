from datetime import datetime
from dataclasses import dataclass


@dataclass
class Position:

	id: int

	symbol: str

	quantity: int

	created_at: datetime

	updated_at: datetime