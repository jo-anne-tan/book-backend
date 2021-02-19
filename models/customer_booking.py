import peewee as pw
import datetime
from models.staff import Staff
from models.customer import Customer
from models.base_model import BaseModel
from models.shop_service import Shop_service

class Customer_booking(BaseModel):
    shop_service = pw.ForeignKeyField(Shop_service, backref="bookings")
    customer = pw.ForeignKeyField(Customer, backref="bookings")
    staff = pw.ForeignKeyField(Staff,backref="bookings")

    # Assuming all services provided are completed within the same day
    date = pw.DateField(null=False)
    time_start = pw.TimeField(null=False)
    time_end = pw.TimeField(null=False)

    # acceptance status by manager/staff
    status = pw.BooleanField(default=False)

    def validate(self):
        pass
        # date check - next day onwards, during shop's operating days
        # time check - during shop's operating hours


    def datetimecheck(self):
        # ---------------------------------------------------------------------
        # Leaving aside for now. May be able to implement this simply by 
        # disabling options based on shop operating hours
        # ---------------------------------------------------------------------

        # This function checks the following:
        # 1. selected booking time is at least 2 hours from now
        # 2. selected booking time is within the shop's business days and hours
        now = datetime.datetime.now()
        two_hours_later = datetime.datetime.now() + timedelta(hours=2)
        weekday = date.weekday()

        if date<now:
            self.errors.append("Selected date must be today or later.")
        if time_start < two_hours_later:
            self.errors.append("Selected start time must be at least 2 hours from now.")
        
        # check operating hours
        # based on weekday num, check shop's corresponding work day and work hours



        
    

