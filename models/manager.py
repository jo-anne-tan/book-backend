import peewee as pw
from models.user import User
from models.shop import Shop

class Manager(User):
    shop = pw.ForeignKeyField(Shop, backref="managers")

    def validate(self):
        # add unique email check
        # invoke super() validate (invoke User validate function)