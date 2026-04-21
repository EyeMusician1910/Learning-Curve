from pydantic import BaseModel,Field,EmailStr

class Baseseller(BaseModel):
    name:str
    email:EmailStr
class SellerRead(Baseseller):
    pass

class SellerCreate(Baseseller):
    password: str = Field(..., min_length=1, max_length=72)
