from pyndantic import BaseModel,Field,EmailStr


class SellerCreate(BaseModel):
    name:str
    email:EmailStr
    password:str