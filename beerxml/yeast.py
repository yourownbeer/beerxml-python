from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class YeastType(str, Enum):
    ale = "Ale"
    lager = "Lager"
    wheat = "Wheat"
    wine = "Wine"
    champagne = "Champagne"


class YeastForm(str, Enum):
    liquid = "Liquid"
    dry = "Dry"
    slant = "Slant"
    culture = "Culture"


class Flocculation(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"
    very_high = "Very High"


class Yeast(BaseModel):
    name: str = Field(alias="NAME")
    version: int = Field(alias="VERSION", ge=1, le=1)
    type: YeastType = Field(alias="TYPE")
    amount: float = Field(alias="AMOUNT", gt=0)
    amount_is_weight: Optional[bool] = Field(alias="AMOUNT_IS_WEIGHT", default=False)
    laboratory: Optional[str] = Field(alias="LABORATORY", default=None)
    product_id: Optional[str] = Field(alias="PRODUCT_ID", default=None)
    min_temperature: Optional[float] = Field(alias="MIN_TEMPERATURE", default=None)
    max_temperature: Optional[float] = Field(alias="MAX_TEMPERATURE", default=None)
    flocculation: Optional[Flocculation] = Field(alias="FLOCCULATION", default=None)
    attenuation: Optional[float] = Field(alias="ATTENUATION", ge=0, le=100, default=None)
    notes: Optional[str] = Field(alias="NOTES", default=None)
    best_for: Optional[str] = Field(alias="BEST_FOR", default=None)
    times_cultured: Optional[int] = Field(alias="TIMES_CULTURED", default=None)
    max_reuse: Optional[int] = Field(alias="MAX_REUSE", default=None)
    add_to_secondary: Optional[bool] = Field(alias="ADD_TO_SECONDARY", default=False)
