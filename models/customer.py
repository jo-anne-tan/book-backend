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
        super().validate() # invokes User's validate function
        self.email_check()


        # add contact_number check
            # +60 ________
            # 10-11 digits including first digit 012 345 6789
            # optional - add phone number otp check (check out pyOTP)

    def email_check(self):
        duplicate = Customer.get(Customer.email==self.email)

        if duplicate:
            if not duplicate.id == self.id: #If the id is not self's id
                self.errors.append("This email is used by another account. Please use another email.")
