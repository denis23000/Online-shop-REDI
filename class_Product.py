from pydantic import BaseModel, Field
import uuid

class Product(BaseModel):
  id: str = Field(default_factory=uuid.uuid4, alias="_id")
  title: str
  description: str
  price: str