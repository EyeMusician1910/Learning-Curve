from datetime import datetime, timedelta, timezone
from binascii import Error as BinasciiError
from fastapi import HTTPException,status
from uuid import uuid4
import jwt

from .services.config import security_settings


def _require_pyjwt() -> None:
    if not all(hasattr(jwt, attr) for attr in ("encode", "decode", "PyJWTError")):
        raise RuntimeError(
            "PyJWT is required for token generation. The active environment has the "
            "'jwt' package installed instead of 'PyJWT'."
        )

def generate_access_token(
    data: dict,
    expiry:timedelta=timedelta(days=1),
) ->str:
    _require_pyjwt()
    return jwt.encode(
            {
                **data,#unpacking a dictionaty
                "jti":uuid4().hex,#giving an unique id to each token created
                "exp":datetime.now(timezone.utc) + expiry,
            },
            key=security_settings.JWT_SECRET,
            algorithm=security_settings.JWT_ALGORITHM,
            )
def decode_access_token(token:str)-> dict | None:
    _require_pyjwt()
    normalized_token = " ".join(token.split())
    if normalized_token.lower().startswith("bearer "):
        normalized_token = normalized_token[7:].strip()
    normalized_token = normalized_token.strip("\"'")
    try:
        return jwt.decode(
            normalized_token,
            key=security_settings.JWT_SECRET,
            algorithms=[security_settings.JWT_ALGORITHM],

        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Expired Access Token",
        )
    except (jwt.PyJWTError, ValueError, TypeError, BinasciiError):
        return None 
