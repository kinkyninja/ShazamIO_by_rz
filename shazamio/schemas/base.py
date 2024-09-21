from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class BaseHref(BaseModel):
    href: str

class BaseIdTypeHref(BaseHref):
    id: str
    type: str

class BaseIdTypeHrefAttributesModel(BaseIdTypeHref):
    attributes: T

class BaseAttributesModel(BaseModel):
    attributes: T

class BaseDataModel(BaseModel):
    data: T

class BaseHrefNextData(BaseHref):
    next: Optional[str] = None
    data: T

class BaseHrefData(BaseHref):
    data: T
