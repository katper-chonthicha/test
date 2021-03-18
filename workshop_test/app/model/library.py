from typing import Optional, List
from pydantic import BaseModel, Field


class createLibraryModel(BaseModel):
    id: str = Field(min_length=5, max_length=5)
    name: str
    publisher: str
    picture_url: str
    stories: List[str]
    price: int


class updateLibraryModel(BaseModel):
    name: Optional[str]
    publisher: Optional[str]
    picture_url: Optional[str]
    stories: Optional[List[str]]
    price: Optional[int]
