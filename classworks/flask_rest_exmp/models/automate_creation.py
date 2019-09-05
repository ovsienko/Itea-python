from models.employee import Employee, Salary, Role

role = {"name": "admin",
        "grade": "high",
        "experience": 3}

salary = {"type": "common",
          "amount": 10000,
          "fees": 900,
          "comment": "salary payment"}

salary_obj = Salary(**salary).save()

employee = {"name": "John", "surname": "Lehnon", "salary_payments": [salary_obj],
            "role": role, }

employee_obj = Employee(**employee).save()
print(employee_obj.to_json())
