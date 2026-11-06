from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import crear_token
from app.db.database import SessionDep
from app.schemas.usuario import UsuarioCreate
from app.services.usuario_service import authenticar_usuario, registrar_usuario

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/register")
def registrar(data: UsuarioCreate, session: SessionDep):
    # Registra un nuevo usuario si el username no existe
    usuario = registrar_usuario(data, session)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario ya existe"
        )
    return usuario


@router.post("/login")
def login(data: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDep):
    # Verifica las credenciales y devuelve un token JWT si son correctas
    usuario = authenticar_usuario(data.username, data.password, session)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrecta",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = crear_token({"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}
