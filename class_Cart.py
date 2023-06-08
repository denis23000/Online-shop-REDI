from pydantic import BaseModel, Field
import uuid

# Cart ---------------------------------------------------------------------------------------------

class Order(BaseModel):
  def __init__(self, id, user_id, product_id):
    self.id = id
    self.user_id = user_id
    self.product_id = product_id




