from sqlmodel import select

from app.core.security import hash_password, verify_password
from app.models.usuario import Usuario


def registrar_usuario(data, session):
    # Verifica que el username no exista antes de crear el usuario
    usuario_existente = session.exec(
        select(Usuario).where(Usuario.username == data.username)
    ).first()

    if usuario_existente:
        return None

    usuario = Usuario(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password),
    )

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario


def authenticar_usuario(username: str, password: str, session):
    # Busca el usuario y verifica que la contraseña sea correcta
    usuario = session.exec(select(Usuario).where(Usuario.username == username)).first()

    if usuario is None:
        return

    if not verify_password(password, usuario.hashed_password):
        return None

    return usuario
