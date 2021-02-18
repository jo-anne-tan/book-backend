import peewee as pw
from models.staff import Staff
from models.customer import Customer
from models.base_model import BaseModel
from models.shop_services import Shop_services

class Customer_booking(BaseModel):
    shop_service = pw.ForeignKeyField(Shop_services, backref="bookings")
    customer = pw.ForeignKeyField(Customer, backref="bookings")
    staff = pw.ForeignKeyField(Staff,backref="bookings")

    # Assuming all services provided can be finished within the same day
    date = pw.DateField(null=False)
    time_start = pw.TimeField(null=False)
    time_end = pw.TimeField(null=False)

    # acceptance status by manager/staff
    status = pw.BooleanField(default=False)

    def validate(self):
        pass
        # date check - next day onwards, during shop's operating days
        # time check - during shop's operating hours


