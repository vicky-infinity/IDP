"""
Pydantic Schemas

Purpose:
---------
Validate incoming request data before it reaches the API.
"""

from pydantic import BaseModel, EmailStr, model_validator


class UserSignup(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords(self):
        """
        Ensure password and confirm_password are identical.
        """
        if self.password != self.confirm_password:
            raise ValueError("Password and Confirm Password do not match.")

        return self