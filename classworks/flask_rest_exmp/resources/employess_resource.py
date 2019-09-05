from flask_restful import Resource
from flask import request
from schemas.employee_schema import EmployeeSchema
from models.employee import Employee as EmployeeModel
from marshmallow import ValidationError


class EmployeeAPI(Resource):

    def get(self, id=None):
        if not id:
            return EmployeeSchema(many=True).dump(EmployeeModel.objects())
        else:
            return EmployeeSchema().dump(
                EmployeeModel.objects.get(id=id))

    def post(self):
        err = EmployeeSchema().validate(request.json)
        if err:
            return err

        employee_obj = EmployeeModel(**request.json).save()
        return EmployeeSchema().dump(employee_obj)

    def put(self, id):
        err = EmployeeSchema().validate(request.json)
        if err:
            raise ValidationError(err)
        employee_obj = EmployeeModel.objects.get(id=id)
        employee_obj.update(**request.json)
        return EmployeeSchema().dump(employee_obj)

    def delete(self, id):
        EmployeeModel.objects.get(id=id).delete()
