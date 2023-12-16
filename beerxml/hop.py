from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class HopUse(str, Enum):
    boil = "Boil"
    dry_hop = "Dry Hop"
    mash = "Mash"
    first_wort = "First Wort"
    aroma = "Aroma"


class HopType(str, Enum):
    bittering = "Bittering"
    aroma = "Aroma"
    both = "Both"


class HopForm(str, Enum):
    pellet = "Pellet"
    plug = "Plug"
    leaf = "Leaf"


class Hop(BaseModel):
    name: str = Field(alias="NAME")
    version: int = Field(alias="VERSION", ge=1, le=1)
    alpha: float = Field(alias="ALPHA", ge=0, le=100)
    amount: float = Field(alias="AMOUNT", gt=0)
    use: HopUse = Field(alias="USE")
    time: int = Field(alias="TIME")
    notes: Optional[str] = Field(alias="NOTES", default=None)
    type: Optional[HopType] = Field(alias="TYPE", default=None)
    form: Optional[HopForm] = Field(alias="FORM", default=None)
    beta: Optional[float] = Field(alias="BETA", ge=1, le=1, default=None)
    hsi: Optional[float] = Field(alias="HSI", ge=1, le=1, default=None)
    origin: Optional[str] = Field(alias="ORIGIN", default=None)
    substitutes: Optional[str] = Field(alias="SUBSTITUTES", default=None)
    humulene: Optional[float] = Field(alias="HUMULENE", ge=1, le=1, default=None)
    caryophyllene: Optional[float] = Field(alias="CARYOPHYLLENE", ge=1, le=1, default=None)
    cohumulone: Optional[float] = Field(alias="COHUMULONE", ge=1, le=1, default=None)
    myrcene: Optional[float] = Field(alias="MYRCENE", ge=1, le=1, default=None)
