from pydantic import BaseModel, Field
import uuid

# Cart ---------------------------------------------------------------------------------------------

class Order(BaseModel):
  id: str = Field(default_factory=uuid.uuid4, alias="_id")
  user_id: str
  product_id: str





