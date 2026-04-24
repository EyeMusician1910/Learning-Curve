from pydantic import BaseModel,Field,EmailStr, field_validator

class Baseseller(BaseModel):
    name:str
    email:EmailStr
class SellerRead(Baseseller):
    pass

class SellerCreate(Baseseller):
    password: str = Field(..., min_length=1, max_length=72)

    @field_validator("password")
    @classmethod
    def validate_password_bytes(cls, value: str) -> str:
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password must be 72 bytes or fewer when UTF-8 encoded")
        return value
