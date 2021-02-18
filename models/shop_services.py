import peewee as pw
from models.shop import Shop
from models.service import Service
from models.base_model import BaseModel

class ShopServices(BaseModel):
    shop = pw.ForeignKeyField(Shop, backref="shops")
    service = pw.ForeignKeyField(Service, backref="services")
    price = pw.DecimalField(null=False)
    range_km = pw.IntegerField(default="10") # 10 km radius from shop location

