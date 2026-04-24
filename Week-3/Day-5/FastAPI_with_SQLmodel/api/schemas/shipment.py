from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from ...database.models import Seller, ShipmentStatus
from sqlmodel import SQLModel,Field



# class ShipmentStatus(str, Enum):
#     placed = "placed"
#     in_transit = "in_transit"
#     out_for_delivery = "out_for_delivery"
#     delivered = "delivered"


class BaseShipment(SQLModel):
    content: str = Field(description="Content of the product", max_length=100)
    weight: float = Field(
        description="Weight of the product in Kgs", le=25, ge=1
    )  # applying conditions such that weight is not more tahn 25kgs and less than 1kg
    destination: int = Field(description="Destination of the shipment")


class ShipmentRead(BaseShipment):
    id:str=Field(default=None,primary_key=True)
    seller : Seller
    status: ShipmentStatus
    estimated_delivery: datetime



class ShipmentCreate(BaseShipment):
    pass#No vlaues need to be given so just pass


class ShipmentUpdate(BaseModel):
    status: ShipmentStatus | None = Field(default=None)
    estimated_delivery: datetime | None = Field(default=None)
    
