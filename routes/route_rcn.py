from fastapi import APIRouter
from models.models_rcn import Noticia
from services.service_rcn import get_noticias

router = APIRouter()

@router.get("/prueba")
async def prueba():
    return {"message": "hola noticias"}

@router.get("/noticias", response_model=list[Noticia])
async def noticias():
    noticias = get_noticias()
    return noticias