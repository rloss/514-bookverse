from fastapi import FastAPI
from app.api.v1 import auth, groups, groups_activities

app = FastAPI()

# ✅ 루트 경로 → API 리스트 제공
@app.get("/")
def root():
    return {
        "message": "📦 Bookverse API is running!",
        "routes": [
            route.path for route in app.routes if route.path.startswith("/api")
        ]
    }

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])
app.include_router(groups_activities.router, prefix="/api/v1/groups-activities", tags=["activities"])