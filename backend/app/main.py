from fastapi import FastAPI
from app.api.v1 import (
    auth, books, comments, groups,
    groups_activities, my, posts,
    users, schedules, user_profile
)

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

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(books.router, prefix="/api/v1/books")
app.include_router(comments.router, prefix="/api/v1/comments")
app.include_router(groups.router, prefix="/api/v1/groups")
app.include_router(groups_activities.router, prefix="/api/v1/groups-activities")
app.include_router(my.router, prefix="/api/v1/my")
app.include_router(posts.router, prefix="/api/v1/posts")
app.include_router(schedules.router, prefix="/api/v1/schedules")
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(user_profile.router, prefix="/api/v1/users/me/profile")