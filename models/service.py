import peewee as pw
from models.base_model import BaseModel

class Service(BaseModel):
    category = pw.CharField(null=False)
    