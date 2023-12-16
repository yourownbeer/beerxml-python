from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FermentableType(str, Enum):
    grain = "Grain"
    sugar = "Sugar"
    extract = "Extract"
    dry_extract = "Dry Extract"
    adjunct = "Adjunct"


class Fermentable(BaseModel):
    name: str = Field(alias="NAME")
    version: int = Field(alias="VERSION", ge=1, le=1)
    type: FermentableType = Field(alias="TYPE")
    amount: float = Field(alias="AMOUNT", gt=0)
    yield_: float = Field(alias="YIELD", ge=1, le=100)
    color: float = Field(alias="COLOR", ge=0)
    add_after_boil: Optional[bool] = Field(alias="ADD_AFTER_BOIL", default=False)
    origin: Optional[str] = Field(alias="ORIGIN", default=None)
    supplier: Optional[str] = Field(alias="SUPPLIER", default=None)
    notes: Optional[str] = Field(alias="NOTES", default=None)
    coarse_fine_diff: Optional[float] = Field(alias="COARSE_FINE_DIFF", ge=0, le=100, default=None)
    moisture: Optional[float] = Field(alias="MOISTURE", ge=0, le=100, default=None)
    diastatic_power: Optional[float] = Field(alias="DIASTATIC_POWER", default=None)
    protein: Optional[float] = Field(alias="PROTEIN", ge=0, le=100, default=None)
    max_in_batch: Optional[float] = Field(alias="MAX_IN_BATCH", ge=0, le=100, default=None)
    recommend_mash: Optional[bool] = Field(alias="RECOMMEND_MASH", default=None)
    ibu_gal_per_lb: Optional[float] = Field(alias="IBU_GAL_PER_LB", default=None)
