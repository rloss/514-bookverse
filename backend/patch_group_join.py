import os

BASE = os.path.join(os.path.dirname(__file__), "app")

schemas_path = os.path.join(BASE, "schemas", "group.py")
api_path = os.path.join(BASE, "api", "v1", "groups.py")
service_path = os.path.join(BASE, "services", "group_service.py")

# 1. schemas/group.py 수정
group_join_request_schema = '''
from pydantic import BaseModel
from uuid import UUID

class GroupJoinRequest(BaseModel):
    group_id: UUID
    message: str | None = None
'''

with open(schemas_path, "a", encoding="utf-8") as f:
    f.write("\n\n" + group_join_request_schema.strip())

# 2. api/v1/groups.py 수정
with open(api_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_join_route = '''
@router.post("/join")
def join_group(
    join_request: GroupJoinRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return request_to_join_group(
        db=db,
        user_id=current_user.id,
        group_id=join_request.group_id,
        message=join_request.message
    )
'''

with open(api_path, "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line)
        if line.strip().startswith("from app.schemas.group"):
            f.write("from app.schemas.group import GroupJoinRequest\n")
    f.write("\n" + new_join_route.strip() + "\n")

# 3. services/group_service.py 수정
with open(service_path, "r", encoding="utf-8") as f:
    content = f.read()

if "def request_to_join_group" in content and "message" not in content:
    content = content.replace(
        "def request_to_join_group(db: Session, user_id: UUID, group_id: UUID):",
        "def request_to_join_group(db: Session, user_id: UUID, group_id: UUID, message: str | None = None):"
    )

with open(service_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ GroupJoinRequest 패치 완료")
