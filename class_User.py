from pydantic import BaseModel, Field
import uuid

class User(BaseModel):
  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email