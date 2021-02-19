import peewee as pw
from models.user import User
from models.shop import Shop

class Manager(User):
    shop = pw.ForeignKeyField(Shop, backref="managers")

    def validate(self):
        super().validate() # invokes User's validate function
        super().email_check(Manager)
