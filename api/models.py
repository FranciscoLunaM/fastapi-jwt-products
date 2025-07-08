from sqlmodel import Field,SQLModel

class Test_table(SQLModel,table=True):
    id: int = Field(default=None,primary_key=True)
    nombre: str
    