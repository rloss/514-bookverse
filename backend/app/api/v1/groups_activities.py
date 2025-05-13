from fastapi import APIRouter

router = APIRouter()

@router.get("/{group_id}/activities")
async def get_group_activities(group_id: str):
    return {"group_id": group_id, "activities": []}
