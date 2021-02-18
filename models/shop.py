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

    # True for work days, false otherwise
    # e.g. if shop operates on Monday only, then only Monday is True
    mon = pw.BooleanField(default=False)
    tue = pw.BooleanField(default=False)
    wed = pw.BooleanField(default=False)
    thu = pw.BooleanField(default=False)
    fri = pw.BooleanField(default=False)
    sat = pw.BooleanField(default=False)
    sun = pw.BooleanField(default=False)

    # Assuming same operating hours on all chosen work days
    # This is either the full operating hours, or the work session before lunch break
    start_time_1 = pw.TimeField(null=False)
    end_time_1 = pw.TimeField(null=False)

    # work session after lunch break. optional.
    start_time_2 = pw.TimeField()
    end_time_2 = pw.TimeField()

    def validate(self):
        pass
        # add postcode check - 5 digits
        # add password check
        # add unique email check