from sqlmodel import select

from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate


def obtener_productos(session):
    return session.exec(select(Producto)).all()


def obtener_producto(id: int, session):
    return session.get(Producto, id)


def crear_producto(data: ProductoCreate, session):
    producto = Producto(**data.model_dump())
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def actualizar_producto(id: int, data: ProductoUpdate, session):
    producto = session.get(Producto, id)

    if producto is None:
        return None

    campos_a_actualizar = data.model_dump(exclude_none=True)
    for campo, valor in campos_a_actualizar.items():
        setattr(producto, campo, valor)

    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def borrar_producto(id: int, session):
    producto = session.get(Producto, id)

    if producto is None:
        return None

    session.delete(producto)
    session.commit()
    return producto
