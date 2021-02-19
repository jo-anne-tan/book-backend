import re
import peewee as pw
from models.base_model import BaseModel

class Service(BaseModel):
    category = pw.CharField(null=False)
    
    def validate(self):
        num = re.search('[\d]',category)
        if num:
            self.errors.append("Please remove numbers")
