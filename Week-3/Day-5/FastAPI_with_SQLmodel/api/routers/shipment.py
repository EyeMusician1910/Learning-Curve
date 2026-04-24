from fastapi import APIRouter, Depends, HTTPException, status
from typing import Any
from FastAPI_with_SQLmodel.api.dependencies import SellerDep, ServiceDep
from FastAPI_with_SQLmodel.api.schemas.shipment import (
    ShipmentCreate,
    ShipmentRead,
    ShipmentUpdate,
)
from FastAPI_with_SQLmodel.database.models import Shipment
from FastAPI_with_SQLmodel.database.session import SessionDep
from FastAPI_with_SQLmodel.services.shipment import ShipmentService

router= APIRouter(prefix="/shipment",tags=["shipment"])#grouping the endpoints together
# router= APIRouter(prefix="/shipment")#applying a prefix
#get content by id
@router.get("/",response_model=ShipmentRead)
async def get_shipment(id: str,session: SessionDep,_:SellerDep,service:ServiceDep) -> dict[str,Any]:#Not type hinting as it's already specified in the response_model parameter #->dict[str,str | int | float] #Type hinting so that the the function takes int as an input and also hinting that the output should be dict which have the key and value of datatype string or integer.
    session
    shipment=await service.get(id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist"
        )
        
    return shipment

#Request Body Pameter
@router.post("/")
async def submit_shipment(shipment: ShipmentCreate, service:ServiceDep,seller:SellerDep)-> Shipment:
   return await service.add(shipment,seller)

@router.patch("/",response_model=ShipmentRead)
async def patch_shipment(id: str, shipment_update:ShipmentUpdate,service:ServiceDep):
    update=shipment_update.model_dump(exclude_unset=True)#the data for which we have to update our shipment
    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data to update"
        )
    shipment=await service.update(id,shipment_update)    
    return shipment

#Delelting a shipment
@router.delete("/")
async def delete_shipment(id:str,service:ServiceDep)-> dict[str,str]:
    await service.delete(id)
    return{"detail": f"ShipmentRead with the id {id} has been deleted"}