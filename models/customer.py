import peewee as pw
from models.user import User

class Customer(User):
    contact_number = pw.CharField(null=False)

    address_line_1 = pw.CharField(null=False)
    address_line_2 = pw.CharField(default="")
    state = pw.CharField(null=False)
    country = pw.CharField(default="Malaysia")
    postcode = pw.CharField(null=False)

    def validate(self):
        pass
        # add unique email check
        # add contact_number check
            # +60 ________
            # 10-11 digits including first digit 012 345 6789
            # optional - add phone number otp check (check out pyOTP)