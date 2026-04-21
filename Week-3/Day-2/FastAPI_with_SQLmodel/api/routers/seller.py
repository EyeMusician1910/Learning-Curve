from fastapi import APIRouter
from ..schemas.seller import SellerModel

router=APIRouter(prefix="seller")

@router.post("/seller/signup")
def register_seller(seller):
    