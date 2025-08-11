from fastapi import FastAPI
from .db import Base, engine
from .routes import items

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registra as rotas
app.include_router(items.router)