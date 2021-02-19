import os
import datetime
import peewee as pw
from database import db

class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default = datetime.datetime.now)
    updated_at = pw.DateTimeField(default = datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.errors=[]
        self.validate()

        if len(self.errors)==0:
            self.updated_at = datetime.datetime.now()
            return super().save(*args, **kwargs)
        else:
            return 0

    def validate(self):
        print(f"Warning, validation method not implemented for {str(type(self))}")
        return True

    def email_check(self, Model):
        duplicate = Model.get(Model.email==self.email)

        if duplicate:
            if not duplicate.id == self.id: #If the id is not self's id
                self.errors.append("This email is used by another account. Please use another email.")

    def password_check(self):
        # conditions:
        # min. 8 char, 1 number, 1 uppercase, 1 lowercase, 1 special character

        length = (len(self.password)>=8)
        special_char = re.search('[\W]', self.password)
        lowercase = re.search('[a-z]',self.password)
        uppercase = re.search('[A-Z]',self.password)
        number = re.search('[0-9]',self.password)

        if not length:
            self.errors.append('Password must be at least 8 characters')
        if not special_char:
            self.errors.append('Password must have at least 1 special character')
        if not lowercase:
            self.errors.append('Password must have at least 1 lowercase')
        if not uppercase:
            self.errors.append('Password must have at least 1 uppercase')
        if not number:
            self.errors.append('Password must have at least 1 number')

    def postcode_check(self):
        valid = re.search('\d{5}$', self.postcode)

    class Meta:
        database=db
        legacy_table_names = False