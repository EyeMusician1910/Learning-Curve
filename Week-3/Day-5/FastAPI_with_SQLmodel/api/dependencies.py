from uuid import UUID

from FastAPI_with_SQLmodel.database.models import Seller
from FastAPI_with_SQLmodel.database.redis import is_jti_blacklisted
from FastAPI_with_SQLmodel.services.seller import SellerService
from FastAPI_with_SQLmodel.services.shipment import ShipmentService
from fastapi import Depends,HTTPException,status
from FastAPI_with_SQLmodel.core.security import oauth2_scheme
from FastAPI_with_SQLmodel.utils import decode_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from FastAPI_with_SQLmodel.database.session import get_session
from typing import Annotated

SessionDep=Annotated[AsyncSession,Depends(get_session)]

def get_shipment_service(session:SessionDep):
    return ShipmentService(session)

ServiceDep=Annotated[ShipmentService,Depends(get_shipment_service)]

def get_seller_service(session:SessionDep):
    return SellerService(session)

SellerServiceDep=Annotated[SellerService,Depends(get_seller_service)]

#access token dependency
async def get_access_token(token: Annotated[str, Depends(oauth2_scheme)])->dict:
    data=decode_access_token(token)

    try:
        token_is_blacklisted = data is not None and await is_jti_blacklisted(data["jti"])
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc

    if data is None or token_is_blacklisted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Access Token",
        )
    return data

#Logged in Seller
async def get_current_seller(
    token_data: Annotated[dict, Depends(get_access_token)],
    session: SessionDep,
):
    return await session.get(Seller, str(token_data["user"]["id"]))


SellerDep=Annotated[Seller,Depends(get_current_seller)]
    
