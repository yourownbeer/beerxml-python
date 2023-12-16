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


class Misc(BaseModel):
    name: str = Field(alias="NAME")
    version: str = Field(alias="VERSION", ge=1, le=1)
    type: MiscType = Field(alias="TYPE")
    use: MiscUse = Field(alias="USE")
    time: int = Field(alias="TIME")
    amount: float = Field(alias="AMOUNT")
    amount_is_weight: Optional[bool] = Field(alias="AMOUNT_IS_WEIGHT", default=False)
    use_for: Optional[str] = Field(alias="USE_FOR")
    notes: Optional[str] = Field(alias="NOTES")
