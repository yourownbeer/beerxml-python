from __future__ import annotations

from enum import Enum
from typing import List, Optional

import pydantic_core
from pydantic import BaseModel, Field, RootModel, field_validator
from typing_extensions import Annotated


class RecipeType(Enum):
    EXTRACT = 'Extract'
    PARTIAL_MASH = 'Partial Mash'
    ALL_GRAIN = 'All Grain'


class StyleType(Enum):
    LAGER = 'Lager'
    ALE = 'Ale'
    MEAD = 'Mead'
    WHEAT = 'Wheat'
    MIXED = 'Mixed'
    CIDER = 'Cider'


class EvapRate(RootModel[float]):
    root: Annotated[float, Field(ge=0.0, le=100.0, title='Evap Rate')]


class HopUtilization(RootModel[float]):
    root: Annotated[float, Field(ge=0.0, le=100.0, title='Hop Utilization')]


class Equipment(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    boil_size: Annotated[float, Field(alias='BOIL_SIZE', title='Boil Size')]
    batch_size: Annotated[float, Field(alias='BATCH_SIZE', title='Batch Size')]
    tun_volume: Annotated[
        Optional[float], Field(alias='TUN_VOLUME', title='Tun Volume')
    ]
    tun_weight: Annotated[
        Optional[float], Field(alias='TUN_WEIGHT', title='Tun Weight')
    ]
    tun_specific_heat: Annotated[
        Optional[float], Field(alias='TUN_SPECIFIC_HEAT', title='Tun Specific Heat')
    ]
    top_up_water: Annotated[
        Optional[float], Field(alias='TOP_UP_WATER', title='Top Up Water')
    ]
    trub_chiller_loss: Annotated[
        Optional[float], Field(alias='TRUB_CHILLER_LOSS', title='Trub Chiller Loss')
    ]
    evap_rate: Annotated[
        Optional[EvapRate], Field(alias='EVAP_RATE', title='Evap Rate')
    ]
    boil_time: Annotated[Optional[float], Field(alias='BOIL_TIME', title='Boil Time')]
    calc_boil_volume: Annotated[
        Optional[bool], Field(alias='CALC_BOIL_VOLUME', title='Calc Boil Volume')
    ]
    lauter_deadspace: Annotated[
        Optional[float], Field(alias='LAUTER_DEADSPACE', title='Lauter Deadspace')
    ]
    top_up_kettle: Annotated[
        Optional[float], Field(alias='TOP_UP_KETTLE', title='Top Up Kettle')
    ]
    hop_utilization: Annotated[
        Optional[HopUtilization],
        Field(alias='HOP_UTILIZATION', title='Hop Utilization'),
    ]
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')]


class Beta(RootModel[float]):
    root: Annotated[float, Field(ge=1.0, le=1.0, title='Beta')]


class Hsi(RootModel[float]):
    root: Annotated[float, Field(ge=1.0, le=1.0, title='Hsi')]


class Humulene(RootModel[float]):
    root: Annotated[float, Field(ge=1.0, le=1.0, title='Humulene')]


class Caryophyllene(RootModel[float]):
    root: Annotated[float, Field(ge=1.0, le=1.0, title='Caryophyllene')]


class Cohumulone(RootModel[float]):
    root: Annotated[float, Field(ge=1.0, le=1.0, title='Cohumulone')]


class Myrcene(RootModel[float]):
    root: Annotated[float, Field(ge=1.0, le=1.0, title='Myrcene')]


class HopUse(Enum):
    BOIL = 'Boil'
    DRY_HOP = 'Dry Hop'
    MASH = 'Mash'
    FIRST_WORT = 'First Wort'
    AROMA = 'Aroma'


class HopType(Enum):
    BITTERING = 'Bittering'
    AROMA = 'Aroma'
    BOTH = 'Both'


class HopForm(Enum):
    PELLET = 'Pellet'
    PLUG = 'Plug'
    LEAF = 'Leaf'


class CoarseFineDiff(RootModel[float]):
    root: Annotated[float, Field(ge=0.0, le=100.0, title='Coarse Fine Diff')]


class Moisture(RootModel[float]):
    root: Annotated[float, Field(ge=0.0, le=100.0, title='Moisture')]


class Protein(RootModel[float]):
    root: Annotated[float, Field(ge=0.0, le=100.0, title='Protein')]


class MaxInBatch(RootModel[float]):
    root: Annotated[float, Field(ge=0.0, le=100.0, title='Max In Batch')]


class FermentableType(Enum):
    GRAIN = 'Grain'
    SUGAR = 'Sugar'
    EXTRACT = 'Extract'
    DRY_EXTRACT = 'Dry Extract'
    ADJUNCT = 'Adjunct'


class MiscType(Enum):
    SPICE = 'Spice'
    FINNING = 'Finning'
    WATER_AGENT = 'Water Agent'
    HERB = 'Herb'
    FLAVOR = 'Flavor'
    OTHER = 'Other'


class MiscUse(Enum):
    BOIL = 'Boil'
    MASH = 'Mash'
    PRIMARY = 'Primary'
    SECONDARY = 'Secondary'
    BOTTLING = 'Bottling'


class Attenuation(RootModel[float]):
    root: Annotated[float, Field(ge=0.0, le=100.0, title='Attenuation')]


class YeastType(Enum):
    ALE = 'Ale'
    LAGER = 'Lager'
    WHEAT = 'Wheat'
    WINE = 'Wine'
    CHAMPAGNE = 'Champagne'


class YeastFlocculation(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    VERY_HIGH = 'Very High'


class Water(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[str, Field(alias='VERSION', title='Version')]
    amount: Annotated[float, Field(alias='AMOUNT', gt=0.0, title='Amount')]
    calcium: Annotated[float, Field(alias='CALCIUM', title='Calcium')]
    bicarbonate: Annotated[float, Field(alias='BICARBONATE', title='Bicarbonate')]
    sulfate: Annotated[float, Field(alias='SULFATE', title='Sulfate')]
    chloride: Annotated[float, Field(alias='CHLORIDE', title='Chloride')]
    sodium: Annotated[float, Field(alias='SODIUM', title='Sodium')]
    magnesium: Annotated[float, Field(alias='MAGNESIUM', title='Magnesium')]
    ph: Annotated[Optional[float], Field(alias='PH', title='Ph')]
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')]


class MashStepType(Enum):
    INFUSION = 'Infusion'
    TEMPERATURE = 'Temperature'
    DECOCTION = 'Decoction'


class Style(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    category: Annotated[str, Field(alias='CATEGORY', title='Category')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    category_number: Annotated[
        int, Field(alias='CATEGORY_NUMBER', title='Category Number')
    ]
    style_letter: Annotated[str, Field(alias='STYLE_LETTER', title='Style Letter')]
    style_guide: Annotated[str, Field(alias='STYLE_GUIDE', title='Style Guide')]
    type: Annotated[StyleType, Field(alias='TYPE')]
    og_min: Annotated[float, Field(alias='OG_MIN', title='Og Min')]
    og_max: Annotated[float, Field(alias='OG_MAX', title='Og Max')]
    fg_min: Annotated[float, Field(alias='FG_MIN', title='Fg Min')]
    fg_max: Annotated[float, Field(alias='FG_MAX', title='Fg Max')]
    ibu_min: Annotated[float, Field(alias='IBU_MIN', title='Ibu Min')]
    ibu_max: Annotated[float, Field(alias='IBU_MAX', title='Ibu Max')]
    color_min: Annotated[float, Field(alias='COLOR_MIN', title='Color Min')]
    color_max: Annotated[float, Field(alias='COLOR_MAX', title='Color Max')]
    carb_min: Annotated[
        Optional[float], Field(None, alias='CARB_MIN', title='Carb Min')
    ]
    carb_max: Annotated[
        Optional[float], Field(None, alias='CARB_MAX', title='Carb Max')
    ]
    abv_min: Annotated[Optional[float], Field(None, alias='ABV_MIN', title='Abv Min')]
    abv_max: Annotated[Optional[float], Field(None, alias='ABV_MAX', title='Abv Max')]
    notes: Annotated[Optional[str], Field(None, alias='NOTES', title='Notes')]
    profile: Annotated[Optional[str], Field(None, alias='PROFILE', title='Profile')]
    ingredients: Annotated[
        Optional[str], Field(None, alias='INGREDIENTS', title='Ingredients')
    ]
    examples: Annotated[Optional[str], Field(None, alias='EXAMPLES', title='Examples')]


class Hop(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    alpha: Annotated[float, Field(alias='ALPHA', ge=0.0, le=100.0, title='Alpha')]
    amount: Annotated[float, Field(alias='AMOUNT', gt=0.0, title='Amount')]
    use: Annotated[HopUse, Field(alias='USE')]
    time: Annotated[int, Field(alias='TIME', title='Time')]
    notes: Annotated[Optional[str], Field(None, alias='NOTES', title='Notes')]
    type: Annotated[Optional[HopType], Field(None, alias='TYPE')]
    form: Annotated[Optional[HopForm], Field(None, alias='FORM')]
    beta: Annotated[Optional[Beta], Field(None, alias='BETA', title='Beta')]
    hsi: Annotated[Optional[Hsi], Field(None, alias='HSI', title='Hsi')]
    origin: Annotated[Optional[str], Field(None, alias='ORIGIN', title='Origin')]
    substitutes: Annotated[
        Optional[str], Field(None, alias='SUBSTITUTES', title='Substitutes')
    ]
    humulene: Annotated[
        Optional[Humulene], Field(None, alias='HUMULENE', title='Humulene')
    ]
    caryophyllene: Annotated[
        Optional[Caryophyllene],
        Field(None, alias='CARYOPHYLLENE', title='Caryophyllene'),
    ]
    cohumulone: Annotated[
        Optional[Cohumulone], Field(None, alias='COHUMULONE', title='Cohumulone')
    ]
    myrcene: Annotated[Optional[Myrcene], Field(None, alias='MYRCENE', title='Myrcene')]


class Fermentable(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[FermentableType, Field(alias='TYPE')]
    amount: Annotated[float, Field(alias='AMOUNT', gt=0.0, title='Amount')]
    yield_: Annotated[float, Field(alias='YIELD', ge=1.0, le=100.0, title='Yield')]
    color: Annotated[float, Field(alias='COLOR', ge=0.0, title='Color')]
    add_after_boil: Annotated[
        Optional[bool], Field(False, alias='ADD_AFTER_BOIL', title='Add After Boil')
    ]
    origin: Annotated[Optional[str], Field(None, alias='ORIGIN', title='Origin')]
    supplier: Annotated[Optional[str], Field(None, alias='SUPPLIER', title='Supplier')]
    notes: Annotated[Optional[str], Field(None, alias='NOTES', title='Notes')]
    coarse_fine_diff: Annotated[
        Optional[CoarseFineDiff],
        Field(None, alias='COARSE_FINE_DIFF', title='Coarse Fine Diff'),
    ]
    moisture: Annotated[
        Optional[Moisture], Field(None, alias='MOISTURE', title='Moisture')
    ]
    diastatic_power: Annotated[
        Optional[float], Field(None, alias='DIASTATIC_POWER', title='Diastatic Power')
    ]
    protein: Annotated[Optional[Protein], Field(None, alias='PROTEIN', title='Protein')]
    max_in_batch: Annotated[
        Optional[MaxInBatch], Field(None, alias='MAX_IN_BATCH', title='Max In Batch')
    ]
    recommend_mash: Annotated[
        Optional[bool], Field(None, alias='RECOMMEND_MASH', title='Recommend Mash')
    ]
    ibu_gal_per_lb: Annotated[
        Optional[float], Field(None, alias='IBU_GAL_PER_LB', title='Ibu Gal Per Lb')
    ]


class Misc(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[str, Field(alias='VERSION', title='Version')]
    type: Annotated[MiscType, Field(alias='TYPE')]
    use: Annotated[MiscUse, Field(alias='USE')]
    time: Annotated[int, Field(alias='TIME', title='Time')]
    amount: Annotated[float, Field(alias='AMOUNT', title='Amount')]
    amount_is_weight: Annotated[
        Optional[bool], Field(False, alias='AMOUNT_IS_WEIGHT', title='Amount Is Weight')
    ]
    use_for: Annotated[Optional[str], Field(None, alias='USE_FOR', title='Use For')]
    notes: Annotated[Optional[str], Field(None, alias='NOTES', title='Notes')]


class Yeast(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[YeastType, Field(alias='TYPE')]
    amount: Annotated[float, Field(alias='AMOUNT', gt=0.0, title='Amount')]
    amount_is_weight: Annotated[
        Optional[bool], Field(False, alias='AMOUNT_IS_WEIGHT', title='Amount Is Weight')
    ]
    laboratory: Annotated[
        Optional[str], Field(None, alias='LABORATORY', title='Laboratory')
    ]
    product_id: Annotated[
        Optional[str], Field(None, alias='PRODUCT_ID', title='Product Id')
    ]
    min_temperature: Annotated[
        Optional[float], Field(None, alias='MIN_TEMPERATURE', title='Min Temperature')
    ]
    max_temperature: Annotated[
        Optional[float], Field(None, alias='MAX_TEMPERATURE', title='Max Temperature')
    ]
    flocculation: Annotated[
        Optional[YeastFlocculation], Field(None, alias='FLOCCULATION')
    ]
    attenuation: Annotated[
        Optional[Attenuation], Field(None, alias='ATTENUATION', title='Attenuation')
    ]
    notes: Annotated[Optional[str], Field(None, alias='NOTES', title='Notes')]
    best_for: Annotated[Optional[str], Field(None, alias='BEST_FOR', title='Best For')]
    times_cultured: Annotated[
        Optional[int], Field(None, alias='TIMES_CULTURED', title='Times Cultured')
    ]
    max_reuse: Annotated[
        Optional[int], Field(None, alias='MAX_REUSE', title='Max Reuse')
    ]
    add_to_secondary: Annotated[
        Optional[bool], Field(False, alias='ADD_TO_SECONDARY', title='Add To Secondary')
    ]


class MashStep(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[MashStepType, Field(alias='TYPE')]
    infuse_amount: Annotated[
        Optional[float], Field(None, alias='INFUSE_AMOUNT', title='Infuse Amount')
    ]
    step_temp: Annotated[float, Field(alias='STEP_TEMP', title='Step Temp')]
    step_time: Annotated[Optional[float], Field(alias='STEP_TIME', title='Step Time')]
    ramp_time: Annotated[
        Optional[int], Field(None, alias='RAMP_TIME', title='Ramp Time')
    ]
    end_temp: Annotated[Optional[int], Field(None, alias='END_TEMP', title='Ramp Time')]


class Mash(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    grain_temp: Annotated[float, Field(alias='GRAIN_TEMP', title='Grain Temp')]
    mash_steps: Annotated[
        Optional[List[MashStep]], Field(alias='MASH_STEPS', title='MashSteps')
    ]
    notes: Annotated[Optional[str], Field(None, alias='NOTES', title='Notes')]
    tun_temp: Annotated[
        Optional[float], Field(None, alias='TUN_TEMP', title='Tun Temp')
    ]
    sparge_temp: Annotated[
        Optional[float], Field(None, alias='SPARGE_TEMP', title='Sparge Temp')
    ]
    ph: Annotated[Optional[float], Field(None, alias='PH', title='Ph')]
    tun_weight: Annotated[
        Optional[float], Field(None, alias='TUN_WEIGHT', title='Tun Weight')
    ]
    tun_specific_heat: Annotated[
        Optional[float],
        Field(None, alias='TUN_SPECIFIC_HEAT', title='Tun Specific Heat'),
    ]
    equip_adjust: Annotated[
        Optional[bool], Field(False, alias='EQUIP_ADJUST', title='Equip Adjust')
    ]

    @field_validator("mash_steps", mode="before")
    def pick_mash_steps(cls, mash_steps):
        mash_steps = mash_steps["MASH_STEP"]
        if isinstance(mash_steps, dict):
            return [mash_steps]
        return mash_steps


class Recipe(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[RecipeType, Field(alias='TYPE')]
    style: Annotated[Style, Field(alias='STYLE')]
    equipment: Annotated[Optional[Equipment], Field(None, alias='EQUIPMENT')]
    brewer: Annotated[str, Field(alias='BREWER', title='Brewer')]
    asst_brewer: Annotated[
        Optional[str], Field(None, alias='ASST_BREWER', title='Asst Brewer')
    ]
    batch_size: Annotated[float, Field(alias='BATCH_SIZE', ge=0.0, title='Batch Size')]
    boil_size: Annotated[float, Field(alias='BOIL_SIZE', ge=0.0, title='Boil Size')]
    boil_time: Annotated[int, Field(alias='BOIL_TIME', ge=0, title='Boil Time')]
    efficiency: Annotated[
        float, Field(alias='EFFICIENCY', ge=0.0, le=100.0, title='Efficiency')
    ]
    hops: Annotated[Optional[List[Hop]], Field(None, alias='HOPS')]
    fermentables: Annotated[
        Optional[List[Fermentable]],
        Field(None, alias='FERMENTABLES', title='Fermentables'),
    ]
    miscs: Annotated[Optional[List[Misc]], Field(None, alias='MISCS', title='Miscs')]
    yeasts: Annotated[
        Optional[List[Yeast]], Field(None, alias='YEASTS', title='Yeasts')
    ]
    waters: Annotated[
        Optional[List[Water]], Field(None, alias='WATERS', title='Waters')
    ]
    mash: Annotated[Mash, Field(alias='MASH')]
    notes: Annotated[Optional[str], Field(None, alias='NOTES', title='Notes')]
    taste_notes: Annotated[
        Optional[str], Field(None, alias='TASTE_NOTES', title='Taste Notes')
    ]
    taste_rating: Annotated[
        Optional[int],
        Field(None, alias='TASTE_RATING', ge=0, le=50, title='Taste Rating'),
    ]
    og: Annotated[Optional[float], Field(None, alias='OG', title='Og')]
    fg: Annotated[Optional[float], Field(None, alias='FG', title='Fg')]
    fermentation_stages: Annotated[
        Optional[int],
        Field(None, alias='FERMENTATION_STAGES', title='Fermentation Stages'),
    ]
    primary_age: Annotated[
        Optional[int], Field(None, alias='PRIMARY_AGE', title='Primary Age')
    ]
    primary_temp: Annotated[
        Optional[int], Field(None, alias='PRIMARY_TEMP', title='Primary Temp')
    ]
    secondary_age: Annotated[
        Optional[int], Field(None, alias='SECONDARY_AGE', title='Secondary Age')
    ]
    secondary_temp: Annotated[
        Optional[int], Field(None, alias='SECONDARY_TEMP', title='Secondary Temp')
    ]
    tertiary_age: Annotated[
        Optional[int], Field(None, alias='TERTIARY_AGE', title='Tertiary Age')
    ]
    tertiary_temp: Annotated[
        Optional[int], Field(None, alias='TERTIARY_TEMP', title='Tertiary Temp')
    ]
    age: Annotated[Optional[int], Field(None, alias='AGE', title='Age')]
    age_temp: Annotated[Optional[int], Field(None, alias='AGE_TEMP', title='Age Temp')]
    date: Annotated[Optional[str], Field(None, alias='DATE', title='Date')]
    carbonation: Annotated[
        Optional[float], Field(None, alias='CARBONATION', title='Carbonation')
    ]
    forced_carbonation: Annotated[
        Optional[bool],
        Field(None, alias='FORCED_CARBONATION', title='Forced Carbonation'),
    ]
    priming_sugar_name: Annotated[
        Optional[str],
        Field(None, alias='PRIMING_SUGAR_NAME', title='Priming Sugar Name'),
    ]
    carbonation_temp: Annotated[
        Optional[float], Field(None, alias='CARBONATION_TEMP', title='Carbonation Temp')
    ]
    priming_sugar_equiv: Annotated[
        Optional[float],
        Field(None, alias='PRIMING_SUGAR_EQUIV', title='Priming Sugar Equiv'),
    ]
    keg_priming_factor: Annotated[
        Optional[float],
        Field(None, alias='KEG_PRIMING_FACTOR', title='Keg Priming Factor'),
    ]

    @field_validator("hops", mode="before")
    def pick_hops(cls, hops):
        try:
            if hops is None:
                return []
            hops = hops["HOP"]
            if isinstance(hops, dict):
                return [hops]
            return hops
        except Exception as err:
            error: pydantic_core.InitErrorDetails = {
                "type": pydantic_core.PydanticCustomError("value_error", str(err)),  # type: ignore
                "loc": ("__root__",),
                "input": hops,
            }
            raise pydantic_core.ValidationError.from_exception_data(cls.__name__, [error]) from err

    @field_validator("fermentables", mode="before")
    def pick_fermentables(cls, fermentables):
        try:
            if fermentables is None:
                return []
            fermentables = fermentables["FERMENTABLE"]
            if isinstance(fermentables, dict):
                return [fermentables]
            return fermentables
        except Exception as err:
            error: pydantic_core.InitErrorDetails = {
                "type": pydantic_core.PydanticCustomError("value_error", str(err)),  # type: ignore
                "loc": ("__root__",),
                "input": fermentables,
            }
            raise pydantic_core.ValidationError.from_exception_data(cls.__name__, [error]) from err

    @field_validator("yeasts", mode="before")
    def pick_yeasts(cls, yeasts):
        try:
            if yeasts is None:
                return []
            yeasts = yeasts["YEAST"]
            if isinstance(yeasts, dict):
                return [yeasts]
            return yeasts
        except Exception as err:
            error: pydantic_core.InitErrorDetails = {
                "type": pydantic_core.PydanticCustomError("value_error", str(err)),  # type: ignore
                "loc": ("__root__",),
                "input": yeasts,
            }
            raise pydantic_core.ValidationError.from_exception_data(cls.__name__, [error]) from err

    @field_validator("miscs", mode="before")
    def pick_miscs(cls, miscs):
        try:
            if miscs is None:
                return []
            miscs = miscs["MISC"]
            if isinstance(miscs, dict):
                return [miscs]
            return miscs
        except Exception as err:
            error: pydantic_core.InitErrorDetails = {
                "type": pydantic_core.PydanticCustomError("value_error", str(err)),  # type: ignore
                "loc": ("__root__",),
                "input": miscs,
            }
            raise pydantic_core.ValidationError.from_exception_data(cls.__name__, [error]) from err

    @field_validator("waters", mode="before")
    def pick_waters(cls, waters):
        try:
            if waters is None:
                return waters
            waters = waters["WATER"]
            if isinstance(waters, dict):
                return [waters]
            return waters
        except Exception as err:
            error: pydantic_core.InitErrorDetails = {
                "type": pydantic_core.PydanticCustomError("value_error", str(err)),  # type: ignore
                "loc": ("__root__",),
                "input": waters,
            }
            raise pydantic_core.ValidationError.from_exception_data(cls.__name__, [error]) from err
