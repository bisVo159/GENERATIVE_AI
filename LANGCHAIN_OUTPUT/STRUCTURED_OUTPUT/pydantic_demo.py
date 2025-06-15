from pydantic import BaseModel, Field,EmailStr
from typing import Optional

# pydantic is a data validation and settings management library for Python, which uses Python type annotations.
# It allows you to define data models with type annotations and provides validation, serialization, and deserialization capabilities.
# Pydantic models are used to define the structure of data, validate it, and convert it to and from various formats like JSON. and also typecast the data to the specified types.
# Pydantic models are useful for ensuring that the data you work with adheres to a specific structure and type, making it easier to catch errors early in the development process.
class Student(BaseModel):
    name: str = Field('anik', description="The name of the student")
    age: Optional[int] = None
    email: EmailStr = Field(...,description="The email address of the student")
    cgpa: float = Field(ge=0.0, le=10.0, default=5,description="The CGPA of the student, must be between 0.0 and 10.0")

new_student = Student(
    # name="John Doe",
    # age=20,
    email="abc123@gmail.com",
    cgpa=9.5)

print(new_student)
print(new_student.model_dump())  # Print the dictionary representation of the student