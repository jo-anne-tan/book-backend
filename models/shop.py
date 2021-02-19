import re
import peewee as pw
from models.base_model import BaseModel

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
        super().email_check(Staff)
        super().password_check()
        super().postcode_check()
        self.time_check()


    def time_check(self):
        if end_time_1<start_time_1:
            self.errors.append("End time cannot be earlier than start time!")

        if end_time_2 and start_time_2:
            if end_time_2<start_time_2:
                self.errors.append("End time cannot be earlier than start time!")
