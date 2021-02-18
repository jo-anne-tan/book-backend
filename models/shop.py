from models.base_model import BaseModel
import peewee as pw

class Shop(BaseModel):
    name = pw.CharField(null=False)
    email = pw.CharField(null=False, unique=True)
    password = pw.CharField(null=False)
    profile_photo = pw.CharField(default="") # to add placeholder profile photo

    address_line_1 = pw.CharField(null=False)
    address_line_2 = pw.CharField(default="")
    state = pw.CharField(null=False)
    country = pw.CharField(default="Malaysia")
    postcode = pw.CharField(null=False)

    def validate(self):
        pass
        # add postcode check - 5 digits
        # add password check
        # add unique email check