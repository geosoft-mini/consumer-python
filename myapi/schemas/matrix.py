from pydantic import BaseModel
from typing import Optional

class Matrix(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None

    