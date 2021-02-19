import peewee as pw
from models.user import User
from models.shop import Shop

class Manager(User):
    shop = pw.ForeignKeyField(Shop, backref="managers")

    def validate(self):
        pass
        # add unique email check
        # invoke super() validate (invoke User validate function)

    def email_check(self):
        duplicate = Manager.get(Manager.email==self.email)

        if duplicate:
            if not duplicate.id == self.id: #If the id is not self's id
                self.errors.append("This email is used by another account. Please use another email.")
