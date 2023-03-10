from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
# import routers.items as items
from routers import items, users, home

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router, tags=["home"], prefix="")
app.include_router(items.router, tags=["items"], prefix="/items")
app.include_router(users.router, tags=["users"], prefix="/users")

if __name__ == '__main__':
    # uvicorn.run(app, host="0.0.0.0", port=38080)
    uvicorn.run(app='main:app', host="0.0.0.0", port=8080, reload=True, workers=2)

