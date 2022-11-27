import get_documents_api

from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/consult/{consult}")
def read_item(consult:str, q: Union[str, None] = None):
    return get_documents_api.send_consult(consult)
