from FastAPI_with_SQLmodel.database.models import Seller
from FastAPI_with_SQLmodel.database.redis import add_jti_to_blacklist
from fastapi import HTTPException,status
from typing import Annotated

from ...utils import decode_access_token
from fastapi import APIRouter
from ..schemas.seller import SellerCreate, SellerRead

from FastAPI_with_SQLmodel.api.dependencies import SellerServiceDep, SessionDep, get_access_token
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
    return {"access_token":token,"token_type":"bearer"} 


###Logout the Seller
@router.get("/logout")
async def logout_seller(token_data:Annotated[dict,Depends(get_access_token)]):
    try:
        await add_jti_to_blacklist(token_data["jti"])
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc

    return{
        "detail":"Successfully logged out"
    }
