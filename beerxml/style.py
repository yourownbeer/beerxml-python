from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class StyleType(str, Enum):
    lager = "Lager"
    ale = "Ale"
    mead = "Mead"
    wheat = "Wheat"
    mixed = "Mixed"
    cider = "Cider"


class Style(BaseModel):
    name: str = Field(alias="NAME")
    category: str = Field(alias="CATEGORY")
    version: int = Field(alias="VERSION", ge=1, le=1)
    category_number: int = Field(alias="CATEGORY_NUMBER")
    style_letter: str = Field(alias="STYLE_LETTER")
    style_guide: str = Field(alias="STYLE_GUIDE")
    type: StyleType = Field(alias="TYPE")
    og_min: float = Field(alias="OG_MIN")
    og_max: float = Field(alias="OG_MAX")
    fg_min: float = Field(alias="FG_MIN")
    fg_max: float = Field(alias="FG_MAX")
    ibu_min: float = Field(alias="IBU_MIN")
    ibu_max: float = Field(alias="IBU_MAX")
    color_min: float = Field(alias="COLOR_MIN")
    color_max: float = Field(alias="COLOR_MAX")
    carb_min: Optional[float] = Field(alias="CARB_MIN", default=None)
    carb_max: Optional[float] = Field(alias="CARB_MAX", default=None)
    abv_min: Optional[float] = Field(alias="ABV_MIN", default=None)
    abv_max: Optional[float] = Field(alias="ABV_MAX", default=None)
    notes: Optional[str] = Field(alias="NOTES", default=None)
    profile: Optional[str] = Field(alias="PROFILE", default=None)
    ingredients: Optional[str] = Field(alias="INGREDIENTS", default=None)
    examples: Optional[str] = Field(alias="EXAMPLES", default=None)
