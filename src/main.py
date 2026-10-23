from fastapi import FastAPI

from src.common import router as common_router

app = FastAPI(title="ToDo list")
app.include_router(common_router)
