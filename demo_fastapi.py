from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
# import routers.items as items
from routers import items, users


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(items.router, tags=["items"], prefix="/items")
app.include_router(users.router, tags=["users"], prefix="/users")

if __name__ == '__main__':
    # uvicorn.run(app, host="0.0.0.0", port=38080)
    uvicorn.run(app='demo_fastapi:app', host="0.0.0.0", port=8080, reload=True, workers=2)
