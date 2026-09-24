from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import faRoutes


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173/",
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
app.include_router(faRoutes.router, prefix="/streamers", tags=["streamers"])


#@app.get("/")