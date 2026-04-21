from typing import Annotated

from fastapi import APIRouter
from ..schemas.seller import SellerCreate, SellerRead

from FastAPI_with_SQLmodel.api.dependencies import SellerServiceDep
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from FastAPI_with_SQLmodel.core.security import oauth2_scheme
router=APIRouter(prefix="/seller",tags=["seller"])

@router.post("/signup",response_model= SellerRead)
async def register_seller(
    seller:SellerCreate,
    service:SellerServiceDep
):
    return await service.add(seller)

#login the seller
@router.post("/token")
async def login_seller(request_form:Annotated[OAuth2PasswordRequestForm ,Depends()],service:SellerServiceDep):
    token = await service.token(request_form.username,request_form.password)
    return {"access_token":token,"type":"jwt"} 

@router.get("/dashboard")
async def get_dashboard(token: Annotated[str, Depends(oauth2_scheme)],):
    return{
        "token":token,
    }
    