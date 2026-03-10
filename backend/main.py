from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from modules.espnData import league


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="http://127.0.0.1:5500",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return FileResponse(os.path.join(os.path.dirname(__file__), "../frontend/index.html"))


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../frontend")), name="static")

#Routes
app.include_router(league.router, prefix="/streamers", tags=["streamers"])


#@app.get("/")