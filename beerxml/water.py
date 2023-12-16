from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MiscType(str, Enum):
    spice = "Spice"
    finning = "Finning"
    water_agent = "Water Agent"
    herb = "herb"
    flavor = "flavor"
    other = "other"


class MiscUse(str, Enum):
    boil = "boil"
    mash = "mash"
    primary = "primary"
    secondary = "secondary"
    bottling = "bottling"


class Water(BaseModel):
    name: str = Field(alias="NAME")
    version: str = Field(alias="VERSION", ge=1, le=1)
    amount: float = Field(alias="AMOUNT", gt=0)
    calcium: float = Field(alias="CALCIUM")
    bicarbonate: float = Field(alias="BICARBONATE")
    sulfate: float = Field(alias="SULFATE")
    chloride: float = Field(alias="CHLORIDE")
    sodium: float = Field(alias="SODIUM")
    magnesium: float = Field(alias="MAGNESIUM")
    ph: Optional[float] = Field(alias="PH")
    notes: Optional[str] = Field(alias="NOTES")
