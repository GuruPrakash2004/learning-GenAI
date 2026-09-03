from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app = FastAPI()

class EmployeeModel(BaseModel):
    name: str
    department: str
    leave_balance:int

employees = {
    101: {
        "name": "Guru",
        "department": "AI",
        "leave_balance": 7
    },
    102: {
        "name": "Arun",
        "department": "IT",
        "leave_balance": 5
    }
}
# get the employeeById
@app.get("/employees/{employee_id}")
def getEmployee(employee_id: int):
    if employee_id not in employees:
        raise HTTPException(status_code=404,detail="employee is not found!")
    return employees[employee_id]


# get all the emploees
@app.get("/employees")
def getAllEmployee():
    return employees


# post the employee
@app.post("/employees")
def createEmployee(employee: EmployeeModel):
    empId = max(employees.keys())+1 if employees else 101
    print(f"{employee.name} is created successfully")
    employees[empId] =  employee.model_dump()
    # print(type(employee))
    return{
        "message": "new Employee is created",
        "empId" : empId,
        "employees": employees
    }





