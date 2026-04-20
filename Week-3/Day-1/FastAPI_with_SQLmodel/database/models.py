from datetime import datetime
from sqlmodel import Field,SQLModel
from enum import Enum




class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

#commenting this out as our schemas is working as the SQLmodel now
# class Shipment(SQLModel, table=True):
#     __tablename__="shipment"
#     id:int =Field(default=None,primary_key=True)
#     content:str
#     weight:float = Field(le=25)
#     destination:int
#     status:ShipmentStatus   
#     estimated_delivery: datetime