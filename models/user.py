import re
import peewee as pw
from models.base_model import BaseModel

class User(BaseModel):
    full_name = pw.CharField(null=False)
    username = pw.CharField(null=False, unique=True)
    email = pw.CharField(null=False, unique=True)
    password = pw.CharField(null=False)

    def validate(self):
        self.password_check()

    def password_check(self):
        # conditions:
        # min. 8 char
        # 1 number
        # 1 uppercase
        # 1 lowercase
        # 1 special character
        length = (len(self.password)>=8)
        special_char = re.search('[\W]', self.password)
        lowercase = re.search('[a-z]',self.password)
        uppercase = re.search('[A-Z]',self.password)
        number = re.search('[0-9]',self.password)

        if !length:
            self.errors.append('Password must be at least 8 characters')
        if !special_char:
            self.errors.append('Password must have at least 1 special character')
        if !lowercase:
            self.errors.append('Password must have at least 1 lowercase')
        if !uppercase:
            self.errors.append('Password must have at least 1 uppercase')
        if !number:
            self.errors.append('Password must have at least 1 number')
            
