from pydantic import BaseModel, Field
import uuid

class Product(BaseModel):
  def __init__(self, id, title, description, price):
      self.id = id
      self.title = title
      self.description = description
      self.price = price