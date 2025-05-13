from enum import Enum

class GroupUserRole(str, Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

class GroupUserStatus(str, Enum):
    active = "active"
    pending = "pending"
    banned = "banned"

class GroupActivityType(str, Enum):
    shared_reading = "shared-reading"
    discussion = "discussion"
    challenge = "challenge"

class GroupActivityStatus(str, Enum):
    planned = "planned"
    active = "active"
    completed = "completed"

class PostCategory(str, Enum):
    review = "review"
    announcement = "announcement"
    community = "community"

class PostVisibility(str, Enum):
    public = "public"
    group_only = "group-only"
    private = "private"
