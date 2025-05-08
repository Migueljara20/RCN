from pydantic import BaseModel

class Noticia(BaseModel):
    titulo: str
    descripcion: str
    media: str
    