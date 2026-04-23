from typing import Annotated

from FastAPI_with_SQLmodel.utils import decode_access_token
from fastapi.security import OAuth2PasswordBearer,HTTPBearer
from fastapi import HTTPException,status,Depends

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/seller/token")
#How OAuth2Really works
# class AccessTokenBearer(HTTPBearer):
#     async def __call__(self,request):
#         auth_credentials= await super().__call__(request)
#         token = auth_credentials.credentials
        
#         token_data=decode_access_token(token)
        
#         if token_data is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Invalid Access Token",
#             )
# access_token_berear=AccessTokenBearer(auto_error=True)

# Annotated[dict,Depends(access_token_berear)]
