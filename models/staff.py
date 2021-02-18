import peewee as pw
from models.user import User
from models.shop import Shop

class Staff(User):
    shop = pw.ForeignKeyField(Shop, backref = "staff")

    def validate(self):
        pass
        # add unique email check