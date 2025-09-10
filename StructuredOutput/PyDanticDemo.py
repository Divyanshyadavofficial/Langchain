# i have to make a dictionary 
# to store a name of a student 
# whose datatype can be string only not other data types are allowed
# i can also validate email strings here 

# feild function -> default values,constraints,description,regex expressions

from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    # type validation is implemented here
    name:str = "Divyansh" #Default value 
    age: Optional[int] = None #Optional value  
    email: EmailStr
    cgpa:float = Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa of the student')

new_Student = {'age':'23','email':'abc@gmail.com','cgpa':5} # type conversion str to int automatically by pydantic

student = Student(**new_Student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()