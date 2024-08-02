from pydantic import BaseModel


class DataItemInSchema(BaseModel):
    key: str
    value: str
