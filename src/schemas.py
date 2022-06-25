from pydantic import BaseModel
from enum import Enum


class Status(Enum):
    success = 'success'
    fail = 'fail'


class ExpressionResult(BaseModel):
    request: str
    response: str
    status: Status
