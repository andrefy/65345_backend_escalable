from fastapi import APIRouter, HTTPException, status

from app.db.database import SessionDep
from app.dependencies.auth import CurrentUser
from app.schemas.producto import ProductoCreate, ProductoUpdate
from app.services import productos_service

router = APIRouter(tags=["Producto"], prefix="/productos")


@router.get("/")
def obtener_productos(current_user: CurrentUser, session: SessionDep):
    return productos_service.obtener_productos(session)


@router.get("/{id}")
def obtener_producto(id: int, current_user: CurrentUser, session: SessionDep):
    producto = productos_service.obtener_producto(id, session)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )

    return producto


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(
    data: ProductoCreate, current_user: CurrentUser, session: SessionDep
):
    return productos_service.crear_producto(data, session)


@router.put("/{id}")
def actualizar_producto(
    id: int, data: ProductoUpdate, current_user: CurrentUser, session: SessionDep
):
    producto = productos_service.actualizar_producto(id, data, session)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )

    return producto


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_producto(id: int, current_user: CurrentUser, session: SessionDep):
    producto = productos_service.borrar_producto(id, session)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
        )
