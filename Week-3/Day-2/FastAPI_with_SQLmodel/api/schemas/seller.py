from pyndantic import BaseModel,Field,EmailStr

class Baseseller(BaseModel):
    name:str
    email:EmailStr
class SellerRead(Baseseller):
    pass

class SellerCreate(Baseseller):
    password: str
