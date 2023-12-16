from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class MashStepType(str, Enum):
    infusion = "Infusion"
    temperature = "Temperature"
    decoction = "Decoction"


class MashStep(BaseModel):
    name: str = Field(alias="NAME")
    version: int = Field(alias="VERSION", ge=1, le=1)
    type: MashStepType = Field(alias="TYPE")
    infuse_amount: Optional[float] = Field(alias="INFUSE_AMOUNT", default=None)
    step_temp: float = Field(alias="STEP_TEMP")
    step_time: int = Field(alias="STEP_TIME")
    ramp_time: Optional[int] = Field(alias="RAMP_TIME", default=None)
    end_temp: Optional[float] = Field(alias="STEP_TIME", default=None)


class Mash(BaseModel):
    name: str = Field(alias="NAME")
    version: int = Field(alias="VERSION", ge=1, le=1)
    grain_temp: float = Field(alias="GRAIN_TEMP")
    mash_steps: list[MashStep] = Field(alias="MASH_STEPS")
    notes: Optional[str] = Field(alias="NOTES", default=None)
    tun_temp: Optional[float] = Field(alias="TUN_TEMP", default=None)
    sparge_temp: Optional[float] = Field(alias="SPARGE_TEMP", default=None)
    ph: Optional[float] = Field(alias="PH", default=None)
    tun_weight: Optional[float] = Field(alias="TUN_WEIGHT", default=None)
    tun_specific_heat: Optional[float] = Field(alias="TUN_SPECIFIC_HEAT", default=None)
    equip_adjust: Optional[bool] = Field(alias="EQUIP_ADJUST", default=False)

    @field_validator("mash_steps", mode="before")
    def pick_mash_steps(cls, mash_steps):
        mash_steps = mash_steps["MASH_STEP"]
        if isinstance(mash_steps, dict):
            return [mash_steps]
        return mash_steps