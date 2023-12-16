import json
from enum import Enum
from typing import Optional

import pydantic_core
from pydantic import BaseModel, Field, field_validator

from beerxml.equipment import Equipment
from beerxml.fermentable import Fermentable
from beerxml.hop import Hop
from beerxml.mash import Mash
from beerxml.misc import Misc
from beerxml.style import Style
from beerxml.water import Water
from beerxml.yeast import Yeast


class NoValidWaterEntriesError(Exception):
    """Indicates that the water entries are not valid"""

class RecipeType(str, Enum):
    extract = "EXTRACT"
    partial_mash = "Partial Mash"
    all_grain = "All Grain"


class Recipe(BaseModel):
    name: str = Field(alias="NAME")
    version: int = Field(alias="VERSION", ge=1, le=1)
    type: RecipeType = Field(alias="TYPE")
    style: Style = Field(alias="STYLE")
    equipment: Optional[Equipment] = Field(alias="EQUIPMENT", default=None)
    brewer: str = Field(alias="BREWER")
    asst_brewer: Optional[str] = Field(alias="ASST_BREWER", default=None)
    batch_size: float = Field(alias="BATCH_SIZE", ge=0)
    boil_size: float = Field(alias="BOIL_SIZE", ge=0)
    boil_time: int = Field(alias="BOIL_TIME", ge=0)
    efficiency: float = Field(alias="EFFICIENCY", ge=0, le=100)
    hops: Optional[list[Hop]] = Field(alias="HOPS", default=None)
    fermentables: Optional[list[Fermentable]] = Field(alias="FERMENTABLES", default=None)
    miscs: Optional[list[Misc]] = Field(alias="MISCS", default=None)
    yeasts: Optional[list[Yeast]] = Field(alias="YEASTS", default=None)
    waters: Optional[list[Water]] = Field(alias="WATERS", default=None)
    mash: Mash = Field(alias="MASH")
    notes: Optional[str] = Field(alias="NOTES", default=None)
    taste_notes: str = Field(alias="TASTE_NOTES", default=None)
    taste_rating: str = Field(alias="TASTE_RATING", default=None)
    og: Optional[float] = Field(alias="OG", default=None)
    fg: Optional[float] = Field(alias="FG", default=None)
    fermentation_stages: Optional[int] = Field(alias="FERMENTATION_STAGES", default=None)
    primary_age: Optional[int] = Field(alias="PRIMARY_AGE", default=None)
    primary_temp: Optional[int] = Field(alias="PRIMARY_TEMP", default=None)
    secondary_age: Optional[int] = Field(alias="SECONDARY_AGE", default=None)
    secondary_temp: Optional[int] = Field(alias="SECONDARY_TEMP", default=None)
    tertiary_age: Optional[int] = Field(alias="TERTIARY_AGE", default=None)
    tertiary_temp: Optional[int] = Field(alias="TERTIARY_TEMP", default=None)
    age: Optional[int] = Field(alias="AGE", default=None)
    age_temp: Optional[int] = Field(alias="AGE_TEMP", default=None)
    date: Optional[str] = Field(alias="DATE", default=None)
    carbonation: Optional[float] = Field(alias="CARBONATION", default=None)
    forced_carbonation: Optional[bool] = Field(alias="FORCED_CARBONATION", default=None)
    priming_sugar_name: Optional[str] = Field(alias="PRIMING_SUGAR_NAME", default=None)
    carbonation_temp: Optional[float] = Field(alias="CARBONATION_TEMP", default=None)
    priming_sugar_equiv: Optional[float] = Field(alias="PRIMING_SUGAR_EQUIV", default=None)
    keg_priming_factor: Optional[float] = Field(alias="KEG_PRIMING_FACTOR", default=None)

    @field_validator("hops", mode="before")
    def pick_hops(cls, hops):
        hops = hops["HOP"]
        if isinstance(hops, dict):
            return [hops]
        return hops

    @field_validator("fermentables", mode="before")
    def pick_fermentables(cls, fermentables):
        fermentables = fermentables["FERMENTABLE"]
        if isinstance(fermentables, dict):
            return [fermentables]
        return fermentables

    @field_validator("yeasts", mode="before")
    def pick_yeasts(cls, yeasts):
        yeasts = yeasts["YEAST"]
        if isinstance(yeasts, dict):
            return [yeasts]
        return yeasts

    @field_validator("waters", mode="before")
    def pick_miscs(cls, waters):
        try:
            if waters is None:
                return waters
            waters = waters["WATER"]
            if isinstance(waters, dict):
                return [waters]
            return waters
        except Exception as err:
            error: pydantic_core.InitErrorDetails = {
                'type': pydantic_core.PydanticCustomError("value_error", str(err)),  # type: ignore
                'loc': ('__root__',),
                'input': waters,
            }
            raise pydantic_core.ValidationError.from_exception_data(cls.__name__, [error])


print(json.dumps(Recipe.model_json_schema()))