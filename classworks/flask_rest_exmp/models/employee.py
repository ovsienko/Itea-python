from mongoengine import *
from models.constants import SALARY_CHOICES

connect("employees")


class Role(EmbeddedDocument):
    name = StringField()
    grade = StringField()
    experience = IntField(min_value=1)


class Salary(Document):
    type = StringField(choices=SALARY_CHOICES)
    amount = IntField(min_value=3200, required=True)
    fees = IntField(required=True)
    comment = StringField(max_length=2048)

    @property
    def net_salary(self):
        return self.amount - self.fees

    @property
    def commentary(self):
        return self.comment

    @commentary.setter
    def commentary(self, value):
        if isinstance(value, str):
            self.comment = value
        else:
            raise TypeError("Wrong type")

    def __str__(self):
        return str(self.id)


class Employee(Document):
    name = StringField(max_length=255)
    surname = StringField(max_length=255)
    email = EmailField()
    salary_payments = ListField(ReferenceField(Salary),  reverse_delete_rule=CASCADE)
    role = EmbeddedDocumentField(Role)

