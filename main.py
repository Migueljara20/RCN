from fastapi import FastAPI
from routes.route_rcn import router as route_rcn

app = FastAPI()

app.include_router(route_rcn, prefix="/rcn")

@app.get("/")
async def root():
    return {"message": "Hola noticias"}

