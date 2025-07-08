import os
from sqlmodel import create_engine,Session

#engine=create_engine("postgresql://username:password@ip:port/dbname", echo=True, connect_args=connect_args)



engine = create_engine("postgresql://root:root@localhost:5432/pruebas", echo=True)

def get_session():
    with Session(engine) as session:
        yield session