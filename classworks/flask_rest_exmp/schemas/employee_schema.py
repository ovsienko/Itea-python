from marshmallow import Schema, fields, validates, ValidationError
from models.employee import Salary, Role, Employee


class RoleSchema(Schema):
    class Meta:
        model = Role
        fields = ('name', 'experience', 'grade')


class EmployeeSchema(Schema):

    salary_payments = fields.List(fields.String())
    role = fields.Nested(RoleSchema)
    id = fields.String(dump_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'role', 'salary_payments')




