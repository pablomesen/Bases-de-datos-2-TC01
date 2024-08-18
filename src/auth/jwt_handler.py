# Este código recibe un token, lo decodifica y lo devuelve si es válido. Si no, devuelve un error 401.

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from .keycloak_config import keycloak_openid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        keycloak_openid.decode_token(token)
        return token
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
