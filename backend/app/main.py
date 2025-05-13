from fastapi import FastAPI
from app.api.v1 import auth, groups

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Bookverse API"}

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])