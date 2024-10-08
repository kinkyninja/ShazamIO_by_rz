from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class BaseHref(BaseModel):
    href: str

class BaseIdTypeHref(BaseHref):
    id: str
    type: str

class BaseIdTypeHrefAttributesModel(BaseIdTypeHref, Generic[T]):
    attributes: T

class BaseAttributesModel(BaseModel, Generic[T]):
    attributes: T

class BaseDataModel(BaseModel, Generic[T]):
    data: T

class BaseHrefNextData(BaseHref, Generic[T]):
    next: Optional[str] = None
    data: T

class BaseHrefData(BaseHref, Generic[T]):
    data: T
