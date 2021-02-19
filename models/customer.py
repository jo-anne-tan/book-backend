import re
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
        self.contact_number_check()

    def email_check(self):
        duplicate = Customer.get(Customer.email==self.email)

        if duplicate:
            if not duplicate.id == self.id: #If the id is not self's id
                self.errors.append("This email is used by another account. Please use another email.")

    def contact_number_check(self):
        # Optional feature - add OTP check with pyOTP
        # checks for mobile number 01x-xxxxxxxx 10 & 11 digit format
        valid = re.search('^[0][1]\d{8,9}$', self.contact_number)

        if not valid:
            self.errors.append("Please enter a valid mobile number")

    def postcode_check(self):
        valid = re.search('\d{5}$', self.postcode)