from pydantic import BaseModel, Field
from enum import Enum
import random


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class BaseShipment(BaseModel):
    content: str = Field(description="Content of the product", max_length=100)
    weight: float = Field(
        description="Weight of the product in Kgs", le=25, ge=1
    )  # applying conditions such that weight is not more tahn 25kgs and less than 1kg


class ShipmentRead(BaseShipment):
    status: ShipmentStatus


class ShipmentCreate(BaseShipment):
    pass#No vlaues need to be given so just pass


class ShipmentUpdate(BaseModel):
    status: ShipmentStatus
