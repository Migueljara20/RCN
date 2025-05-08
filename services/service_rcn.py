from fastapi import FastAPI
from models.models_rcn import Noticia
from bs4 import BeautifulSoup
import requests

def get_noticias():
    url = "https://www.noticiasrcn.com/colombia"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    noticias = []


    for quote_block in soup.find_all("div", class_ ="post-h"):
        
        titulo_noticia = quote_block.find("h3", class_="title").text
        
        
        descripcion = quote_block.find("p", class_="lead").text
        
        media = quote_block.find("a", class_="img-a").get("href")
          

        noticias.append({
        "titulo": titulo_noticia,
        "descripcion": descripcion,
        "media": media,
    })    

    
    
    return noticias


