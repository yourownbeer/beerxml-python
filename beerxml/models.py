from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class RecipeType(Enum):
    EXTRACT = 'EXTRACT'
    PARTIAL_MASH = 'Partial Mash'
    ALL_GRAIN = 'All Grain'


class StyleType(Enum):
    LAGER = 'Lager'
    ALE = 'Ale'
    MEAD = 'Mead'
    WHEAT = 'Wheat'
    MIXED = 'Mixed'
    CIDER = 'Cider'


class EvapRate(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0, title='Evap Rate')]


class HopUtilization(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0, title='Hop Utilization')]


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


class Beta(BaseModel):
    __root__: Annotated[float, Field(ge=1.0, le=1.0, title='Beta')]


class Hsi(BaseModel):
    __root__: Annotated[float, Field(ge=1.0, le=1.0, title='Hsi')]


class Humulene(BaseModel):
    __root__: Annotated[float, Field(ge=1.0, le=1.0, title='Humulene')]


class Caryophyllene(BaseModel):
    __root__: Annotated[float, Field(ge=1.0, le=1.0, title='Caryophyllene')]


class Cohumulone(BaseModel):
    __root__: Annotated[float, Field(ge=1.0, le=1.0, title='Cohumulone')]


class Myrcene(BaseModel):
    __root__: Annotated[float, Field(ge=1.0, le=1.0, title='Myrcene')]


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


class CoarseFineDiff(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0, title='Coarse Fine Diff')]


class Moisture(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0, title='Moisture')]


class Protein(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0, title='Protein')]


class MaxInBatch(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0, title='Max In Batch')]


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
    HERB = 'herb'
    FLAVOR = 'flavor'
    OTHER = 'other'


class MiscUse(Enum):
    BOIL = 'boil'
    MASH = 'mash'
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    BOTTLING = 'bottling'


class Attenuation(BaseModel):
    __root__: Annotated[float, Field(ge=0.0, le=100.0, title='Attenuation')]


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
    carb_min: Annotated[Optional[float], Field(alias='CARB_MIN', title='Carb Min')] = (
        None
    )
    carb_max: Annotated[Optional[float], Field(alias='CARB_MAX', title='Carb Max')] = (
        None
    )
    abv_min: Annotated[Optional[float], Field(alias='ABV_MIN', title='Abv Min')] = None
    abv_max: Annotated[Optional[float], Field(alias='ABV_MAX', title='Abv Max')] = None
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')] = None
    profile: Annotated[Optional[str], Field(alias='PROFILE', title='Profile')] = None
    ingredients: Annotated[
        Optional[str], Field(alias='INGREDIENTS', title='Ingredients')
    ] = None
    examples: Annotated[Optional[str], Field(alias='EXAMPLES', title='Examples')] = None


class Hop(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    alpha: Annotated[float, Field(alias='ALPHA', ge=0.0, le=100.0, title='Alpha')]
    amount: Annotated[float, Field(alias='AMOUNT', gt=0.0, title='Amount')]
    use: Annotated[HopUse, Field(alias='USE')]
    time: Annotated[int, Field(alias='TIME', title='Time')]
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')] = None
    type: Annotated[Optional[HopType], Field(alias='TYPE')] = None
    form: Annotated[Optional[HopForm], Field(alias='FORM')] = None
    beta: Annotated[Optional[Beta], Field(alias='BETA', title='Beta')] = None
    hsi: Annotated[Optional[Hsi], Field(alias='HSI', title='Hsi')] = None
    origin: Annotated[Optional[str], Field(alias='ORIGIN', title='Origin')] = None
    substitutes: Annotated[
        Optional[str], Field(alias='SUBSTITUTES', title='Substitutes')
    ] = None
    humulene: Annotated[
        Optional[Humulene], Field(alias='HUMULENE', title='Humulene')
    ] = None
    caryophyllene: Annotated[
        Optional[Caryophyllene], Field(alias='CARYOPHYLLENE', title='Caryophyllene')
    ] = None
    cohumulone: Annotated[
        Optional[Cohumulone], Field(alias='COHUMULONE', title='Cohumulone')
    ] = None
    myrcene: Annotated[Optional[Myrcene], Field(alias='MYRCENE', title='Myrcene')] = (
        None
    )


class Fermentable(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[FermentableType, Field(alias='TYPE')]
    amount: Annotated[float, Field(alias='AMOUNT', gt=0.0, title='Amount')]
    yield_: Annotated[float, Field(alias='YIELD', ge=1.0, le=100.0, title='Yield')]
    color: Annotated[float, Field(alias='COLOR', ge=0.0, title='Color')]
    add_after_boil: Annotated[
        Optional[bool], Field(alias='ADD_AFTER_BOIL', title='Add After Boil')
    ] = False
    origin: Annotated[Optional[str], Field(alias='ORIGIN', title='Origin')] = None
    supplier: Annotated[Optional[str], Field(alias='SUPPLIER', title='Supplier')] = None
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')] = None
    coarse_fine_diff: Annotated[
        Optional[CoarseFineDiff],
        Field(alias='COARSE_FINE_DIFF', title='Coarse Fine Diff'),
    ] = None
    moisture: Annotated[
        Optional[Moisture], Field(alias='MOISTURE', title='Moisture')
    ] = None
    diastatic_power: Annotated[
        Optional[float], Field(alias='DIASTATIC_POWER', title='Diastatic Power')
    ] = None
    protein: Annotated[Optional[Protein], Field(alias='PROTEIN', title='Protein')] = (
        None
    )
    max_in_batch: Annotated[
        Optional[MaxInBatch], Field(alias='MAX_IN_BATCH', title='Max In Batch')
    ] = None
    recommend_mash: Annotated[
        Optional[bool], Field(alias='RECOMMEND_MASH', title='Recommend Mash')
    ] = None
    ibu_gal_per_lb: Annotated[
        Optional[float], Field(alias='IBU_GAL_PER_LB', title='Ibu Gal Per Lb')
    ] = None


class Misc(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[str, Field(alias='VERSION', title='Version')]
    type: Annotated[MiscType, Field(alias='TYPE')]
    use: Annotated[MiscUse, Field(alias='USE')]
    time: Annotated[int, Field(alias='TIME', title='Time')]
    amount: Annotated[float, Field(alias='AMOUNT', title='Amount')]
    amount_is_weight: Annotated[
        Optional[bool], Field(alias='AMOUNT_IS_WEIGHT', title='Amount Is Weight')
    ] = False
    use_for: Annotated[Optional[str], Field(alias='USE_FOR', title='Use For')]
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')]


class Yeast(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[YeastType, Field(alias='TYPE')]
    amount: Annotated[float, Field(alias='AMOUNT', gt=0.0, title='Amount')]
    amount_is_weight: Annotated[
        Optional[bool], Field(alias='AMOUNT_IS_WEIGHT', title='Amount Is Weight')
    ] = False
    laboratory: Annotated[
        Optional[str], Field(alias='LABORATORY', title='Laboratory')
    ] = None
    product_id: Annotated[
        Optional[str], Field(alias='PRODUCT_ID', title='Product Id')
    ] = None
    min_temperature: Annotated[
        Optional[float], Field(alias='MIN_TEMPERATURE', title='Min Temperature')
    ] = None
    max_temperature: Annotated[
        Optional[float], Field(alias='MAX_TEMPERATURE', title='Max Temperature')
    ] = None
    flocculation: Annotated[
        Optional[YeastFlocculation], Field(alias='FLOCCULATION')
    ] = None
    attenuation: Annotated[
        Optional[Attenuation], Field(alias='ATTENUATION', title='Attenuation')
    ] = None
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')] = None
    best_for: Annotated[Optional[str], Field(alias='BEST_FOR', title='Best For')] = None
    times_cultured: Annotated[
        Optional[int], Field(alias='TIMES_CULTURED', title='Times Cultured')
    ] = None
    max_reuse: Annotated[Optional[int], Field(alias='MAX_REUSE', title='Max Reuse')] = (
        None
    )
    add_to_secondary: Annotated[
        Optional[bool], Field(alias='ADD_TO_SECONDARY', title='Add To Secondary')
    ] = False


class Waters(BaseModel):
    water: Annotated[Optional[List[Water]], Field(alias='WATER', title='Water')]


class MashStep(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[MashStepType, Field(alias='TYPE')]
    infuse_amount: Annotated[
        Optional[float], Field(alias='INFUSE_AMOUNT', title='Infuse Amount')
    ] = None
    step_temp: Annotated[float, Field(alias='STEP_TEMP', title='Step Temp')]
    step_time: Annotated[Optional[float], Field(alias='STEP_TIME', title='Step Time')]
    ramp_time: Annotated[Optional[int], Field(alias='RAMP_TIME', title='Ramp Time')] = (
        None
    )


class Hops(BaseModel):
    hop: Annotated[Optional[List[Hop]], Field(alias='HOP', title='Hop')]


class Fermentables(BaseModel):
    fermentable: Annotated[
        Optional[List[Fermentable]], Field(alias='FERMENTABLE', title='Fermentable')
    ]


class Miscs(BaseModel):
    misc: Annotated[Optional[List[Misc]], Field(alias='MISC', title='Misc')]


class Yeasts(BaseModel):
    yeast: Annotated[Optional[List[Yeast]], Field(alias='YEAST', title='Yeast')]


class MashSteps(BaseModel):
    mash_step: Annotated[
        Optional[List[MashStep]], Field(alias='MASH_STEP', title='MashStep')
    ]


class Mash(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    grain_temp: Annotated[float, Field(alias='GRAIN_TEMP', title='Grain Temp')]
    mash_steps: Annotated[MashSteps, Field(alias='MASH_STEPS')]
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')] = None
    tun_temp: Annotated[Optional[float], Field(alias='TUN_TEMP', title='Tun Temp')] = (
        None
    )
    sparge_temp: Annotated[
        Optional[float], Field(alias='SPARGE_TEMP', title='Sparge Temp')
    ] = None
    ph: Annotated[Optional[float], Field(alias='PH', title='Ph')] = None
    tun_weight: Annotated[
        Optional[float], Field(alias='TUN_WEIGHT', title='Tun Weight')
    ] = None
    tun_specific_heat: Annotated[
        Optional[float], Field(alias='TUN_SPECIFIC_HEAT', title='Tun Specific Heat')
    ] = None
    equip_adjust: Annotated[
        Optional[bool], Field(alias='EQUIP_ADJUST', title='Equip Adjust')
    ] = False


class Recipe(BaseModel):
    name: Annotated[str, Field(alias='NAME', title='Name')]
    version: Annotated[int, Field(alias='VERSION', ge=1, le=1, title='Version')]
    type: Annotated[RecipeType, Field(alias='TYPE')]
    style: Annotated[Style, Field(alias='STYLE')]
    equipment: Annotated[Optional[Equipment], Field(alias='EQUIPMENT')] = None
    brewer: Annotated[str, Field(alias='BREWER', title='Brewer')]
    asst_brewer: Annotated[
        Optional[str], Field(alias='ASST_BREWER', title='Asst Brewer')
    ] = None
    batch_size: Annotated[float, Field(alias='BATCH_SIZE', ge=0.0, title='Batch Size')]
    boil_size: Annotated[float, Field(alias='BOIL_SIZE', ge=0.0, title='Boil Size')]
    boil_time: Annotated[int, Field(alias='BOIL_TIME', ge=0, title='Boil Time')]
    efficiency: Annotated[
        float, Field(alias='EFFICIENCY', ge=0.0, le=100.0, title='Efficiency')
    ]
    hops: Annotated[Optional[Hops], Field(alias='HOPS')] = None
    fermentables: Annotated[
        Optional[Fermentables], Field(alias='FERMENTABLES', title='Fermentables')
    ] = None
    miscs: Annotated[Optional[Miscs], Field(alias='MISCS', title='Miscs')] = None
    yeasts: Annotated[Optional[Yeasts], Field(alias='YEASTS', title='Yeasts')] = None
    waters: Annotated[Optional[Waters], Field(alias='WATERS', title='Waters')] = None
    mash: Annotated[Mash, Field(alias='MASH')]
    notes: Annotated[Optional[str], Field(alias='NOTES', title='Notes')] = None
    taste_notes: Annotated[
        Optional[str], Field(alias='TASTE_NOTES', title='Taste Notes')
    ] = None
    taste_rating: Annotated[
        Optional[str], Field(alias='TASTE_RATING', title='Taste Rating')
    ] = None
    og: Annotated[Optional[float], Field(alias='OG', title='Og')] = None
    fg: Annotated[Optional[float], Field(alias='FG', title='Fg')] = None
    fermentation_stages: Annotated[
        Optional[int], Field(alias='FERMENTATION_STAGES', title='Fermentation Stages')
    ] = None
    primary_age: Annotated[
        Optional[int], Field(alias='PRIMARY_AGE', title='Primary Age')
    ] = None
    primary_temp: Annotated[
        Optional[int], Field(alias='PRIMARY_TEMP', title='Primary Temp')
    ] = None
    secondary_age: Annotated[
        Optional[int], Field(alias='SECONDARY_AGE', title='Secondary Age')
    ] = None
    secondary_temp: Annotated[
        Optional[int], Field(alias='SECONDARY_TEMP', title='Secondary Temp')
    ] = None
    tertiary_age: Annotated[
        Optional[int], Field(alias='TERTIARY_AGE', title='Tertiary Age')
    ] = None
    tertiary_temp: Annotated[
        Optional[int], Field(alias='TERTIARY_TEMP', title='Tertiary Temp')
    ] = None
    age: Annotated[Optional[int], Field(alias='AGE', title='Age')] = None
    age_temp: Annotated[Optional[int], Field(alias='AGE_TEMP', title='Age Temp')] = None
    date: Annotated[Optional[str], Field(alias='DATE', title='Date')] = None
    carbonation: Annotated[
        Optional[float], Field(alias='CARBONATION', title='Carbonation')
    ] = None
    forced_carbonation: Annotated[
        Optional[bool], Field(alias='FORCED_CARBONATION', title='Forced Carbonation')
    ] = None
    priming_sugar_name: Annotated[
        Optional[str], Field(alias='PRIMING_SUGAR_NAME', title='Priming Sugar Name')
    ] = None
    carbonation_temp: Annotated[
        Optional[float], Field(alias='CARBONATION_TEMP', title='Carbonation Temp')
    ] = None
    priming_sugar_equiv: Annotated[
        Optional[float], Field(alias='PRIMING_SUGAR_EQUIV', title='Priming Sugar Equiv')
    ] = None
    keg_priming_factor: Annotated[
        Optional[float], Field(alias='KEG_PRIMING_FACTOR', title='Keg Priming Factor')
    ] = None
