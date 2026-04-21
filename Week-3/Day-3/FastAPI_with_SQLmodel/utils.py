import jwt
from datetime import datetime, timedelta
from .config import security_settings

def generate_access_token():
    jwt.encode(
            payload={
                "user":{
                    "name":seller.name,
                    "email":seller.email,
                },
                "exp":datetime.now() + timedelta(days=1)
            },
            algorithm=security_settings.JWT_ALGORITHM,
            key=security_settings.JWT_SECRET,
            )
def decode_access_token():
    pass