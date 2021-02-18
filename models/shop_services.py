import peewee as pw
from models.shop import Shop
from models.service import Service
from models.base_model import BaseModel

class Shop_services(BaseModel):
    shop = pw.ForeignKeyField(Shop, backref="shops")
    service = pw.ForeignKeyField(Service, backref="services")
    price = pw.DecimalField(null=False)
    range_km = pw.IntegerField(default="10") # 10 km radius from shop location
    door_service = pw.BooleanType(default=False)
    store_service = pw.BooleanType(default=True)

    def validate(self):
        pass
        # add range check 
            # no negative numbers
            # no more than 50km
            # door_service must be True
        # add price check - no negative numbers
        # add door_service check
            # range_km must be Truthy