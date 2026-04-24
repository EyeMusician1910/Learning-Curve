from datetime import datetime
from enum import Enum
from uuid import uuid4

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class Shipment(SQLModel, table=True):
    __tablename__ = "shipment"
    __table_args__ = {"extend_existing": True}

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    content: str
    weight: float = Field(le=25)
    destination: int
    status: ShipmentStatus
    estimated_delivery: datetime
    seller_id: str = Field(foreign_key="seller.id")

    seller: "Seller" = Relationship(
        back_populates="shipments",
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class Seller(SQLModel, table=True):
    __tablename__ = "seller"
    __table_args__ = {"extend_existing": True}

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    address:int
    email: EmailStr
    password_hash: str

    shipments: list["Shipment"] = Relationship(
        back_populates="seller",
        sa_relationship_kwargs={"lazy": "selectin"},
    )
