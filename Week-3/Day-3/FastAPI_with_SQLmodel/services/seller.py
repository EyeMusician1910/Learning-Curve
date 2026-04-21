from datetime import datetime, timedelta

from FastAPI_with_SQLmodel.api.schemas.seller import SellerCreate
from FastAPI_with_SQLmodel.database.models import Seller
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from sqlalchemy import select
from fastapi import HTTPException,status
from .config import security_settings
import jwt

password_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
class SellerService:
    def __init__(self,session:AsyncSession):
        self.session=session
    async def add(self,credentials:SellerCreate)-> Seller:
        print(credentials.password)
        print(type(credentials.password))
        print(len(credentials.password))
        print(len(credentials.password.encode("utf-8")))
        seller=Seller(
            **credentials.model_dump(exclude=["password"]),
            #Hashed Passoword
            password_hash=password_context.hash(credentials.password),
        
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
        if seller is None or not password_context.verify(
            password,
            seller.password_hash,
        ):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="email or password is incorrect"
                )
        token = 
        
        jwt.decode(
            "token",
            
        )
        
        return token

            
        
        