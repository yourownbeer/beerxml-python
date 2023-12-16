from typing import Optional

from pydantic import BaseModel, Field


class Equipment(BaseModel):
    name: str = Field(alias="NAME")
    version: int = Field(alias="VERSION", ge=1, le=1)
    boil_size: float = Field(alias="BOIL_SIZE")
    batch_size: float = Field(alias="BATCH_SIZE")
    tun_volume: Optional[float] = Field(alias="TUN_VOLUME")
    tun_weight: Optional[float] = Field(alias="TUN_WEIGHT")
    tun_specific_heat: Optional[float] = Field(alias="TUN_SPECIFIC_HEAT")
    top_up_water: Optional[float] = Field(alias="TOP_UP_WATER")
    trub_chiller_loss: Optional[float] = Field(alias="TRUB_CHILLER_LOSS")
    evap_rate: Optional[float] = Field(alias="EVAP_RATE", ge=0, le=100)
    boil_time: Optional[float] = Field(alias="BOIL_TIME")
    calc_boil_volume: Optional[bool] = Field(alias="CALC_BOIL_VOLUME")
    lauter_deadspace: Optional[float] = Field(alias="LAUTER_DEADSPACE")
    top_up_kettle: Optional[float] = Field(alias="TOP_UP_KETTLE")
    hop_utilization: Optional[float] = Field(alias="HOP_UTILIZATION", ge=0, le=100)
    notes: Optional[str] = Field(alias="NOTES")
