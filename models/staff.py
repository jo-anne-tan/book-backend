import peewee as pw
from models.user import User
from models.shop import Shop

class Staff(User):
    shop = pw.ForeignKeyField(Shop, backref = "staff")

    def validate(self):
        super().validate() # invokes User's validate function
        self.email_check()

    def email_check(self):
        duplicate = Staff.get(Staff.email==self.email)

        if duplicate:
            if not duplicate.id == self.id: #If the id is not self's id
                self.errors.append("This email is used by another account. Please use another email.")
