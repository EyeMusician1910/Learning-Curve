from datetime import datetime, timedelta

from FastAPI_with_SQLmodel.api.schemas.shipment import ShipmentCreate, ShipmentUpdate
from FastAPI_with_SQLmodel.database.models import Shipment, ShipmentStatus
from sqlalchemy.ext.asyncio import AsyncSession



class ShipmentService:
    def __init__(self,session:AsyncSession):
        self.session=session
    async def get(self,id: int) -> Shipment:
        return await self.session.get(Shipment,id)
    async def add(self,shipment_create:ShipmentCreate)-> Shipment:
        new_shipment=Shipment(
            **shipment_create.model_dump(),
            status=ShipmentStatus.placed,
            estimated_delivery=datetime.now() + timedelta(days=3)
        )
        self.session.add(new_shipment)#adding the new data into the db
        await self.session.commit()#commiting the changes
        await self.session.refresh(new_shipment)#need to refresh the db to get the id
        return new_shipment
        
    async def update(self,id:int, shipment_update:ShipmentUpdate)-> Shipment:
        shipment=await self.get(id)
        shipment.sqlmodel_update(shipment_update)#we can use this as it's already a sqlmodel
        self.session.add(shipment)#adding the updated values
        await self.session.commit()#commiting the changes
        await self.session.refresh(shipment)#refreshing to the updated values
        return shipment
    async def delete(self,id:int)-> None:
        await self.session.delete(
        await self.get(id)
        )
        await self.session.commit()
    