# backend/app/schemas.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class RecordTimeIn(BaseModel):
    start_number: str
    station: str

class UpdateTimeIn(BaseModel):
    id: int
    new_time: datetime

class CompetitorIn(BaseModel):
    start_number: str
    name: str

class CompetitorOut(BaseModel):
    id: int
    start_number: str
    name: str

    model_config = ConfigDict(from_attributes=True)


class TimeEntryOut(BaseModel):
    id: int
    competitor_id: int
    timestamp: datetime
    station :str

    model_config = ConfigDict(from_attributes=True)
