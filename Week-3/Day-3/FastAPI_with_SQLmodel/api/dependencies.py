from FastAPI_with_SQLmodel.services.seller import SellerService
from FastAPI_with_SQLmodel.services.shipment import ShipmentService
from fastapi import Depends
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