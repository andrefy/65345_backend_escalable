from sqlmodel import Field, SQLModel


class UsuarioCreate(SQLModel):
    username: str = Field(min_length=3)
    email: str
    password: str = Field(min_length=3)
