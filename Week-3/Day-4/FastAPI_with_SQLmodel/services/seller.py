from datetime import datetime, timedelta

import bcrypt
from FastAPI_with_SQLmodel.api.schemas.seller import SellerCreate
from FastAPI_with_SQLmodel.database.models import Seller
from FastAPI_with_SQLmodel.utils import generate_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException,status
from .config import security_settings


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Password must be 72 bytes or fewer when UTF-8 encoded",
        )
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    password_bytes = password.encode("utf-8")
    if len(password_bytes) > 72:
        return False
    return bcrypt.checkpw(password_bytes, password_hash.encode("utf-8"))


class SellerService:
    def __init__(self,session:AsyncSession):
        self.session=session
    async def add(self,credentials:SellerCreate)-> Seller:
        seller=Seller(
            **credentials.model_dump(exclude=["password"]),
            #Hashed Passoword
            password_hash=hash_password(credentials.password),
        
        )
        self.session.add(seller)
        await self.session.commit()
        await self.session.refresh(seller)
        
        return seller 
    
    async def token(self,email,password)->str:
        #Validate the user
        result=await self.session.execute(
        select(Seller).where(Seller.email==email)
        )
        seller =result.scalar()
        is_valid = seller is not None and verify_password(
            password,
            seller.password_hash,
        )

        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="email or password is incorrect"
                )
        token = generate_access_token(data={
            "user":{
                "name":seller.name,
                "id": seller.id,
            }
        })
        

        
        return token

            
        
        

