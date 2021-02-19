import re
import peewee as pw
from models.base_model import BaseModel

class User(BaseModel):
    full_name = pw.CharField(null=False)
    username = pw.CharField(null=False, unique=True)
    email = pw.CharField(null=False, unique=True)
    password = pw.CharField(null=False)

    def validate(self):
        super().password_check()
