from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
	item_id: int
	item_content: Optional[str]
