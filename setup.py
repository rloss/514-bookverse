import os

BASE_DIRS = [
    # Root level
    "backend/app/api/v1",
    "backend/app/core",
    "backend/app/models",
    "backend/app/schemas",
    "backend/app/services",
    "backend/app/db",
    "backend/app/utils",
    "backend/tests",
    "backend/alembic/versions",
    "frontend/app/books/[bookId]",
    "frontend/app/groups/[groupId]/books",
    "frontend/app/groups/[groupId]/posts",
    "frontend/app/groups/[groupId]/calendar",
    "frontend/app/groups/[groupId]/members",
    "frontend/app/groups/[groupId]/my",
    "frontend/app/groups/[groupId]/settings",
    "frontend/app/login",
    "frontend/app/signup",
    "frontend/app/write",
    "frontend/app/my/books",
    "frontend/app/my/posts",
    "frontend/app/my/groups",
    "frontend/app/my/settings",
    "frontend/components/layout",
    "frontend/components/auth",
    "frontend/components/post",
    "frontend/components/group",
    "frontend/components/book",
    "frontend/components/ui",
    "frontend/lib/api",
    "frontend/styles",
    "frontend/public",
    "docs"
]

FILES_TO_CREATE = [
    "backend/app/main.py",
    "backend/requirements.txt",
    "frontend/package.json",
    "frontend/next.config.js",
    "frontend/tailwind.config.ts",
    "frontend/postcss.config.js",
    "frontend/tsconfig.json",
    "frontend/.env.production",
    "README.md",
    ".gitignore"
]

FOLDER_FILES = {
    "backend/app/api/v1": ["auth.py", "users.py", "groups.py", "posts.py", "books.py", "comments.py", "schedules.py", "activities.py"],
    "backend/app/core": ["config.py", "security.py", "logging.py", "exceptions.py"],
    "backend/app/models": ["user.py", "group.py", "activity.py", "post.py", "book.py", "schedule.py", "comment.py", "social_account.py", "base.py"],
    "backend/app/schemas": ["user.py", "group.py", "activity.py", "post.py", "book.py", "comment.py", "schedule.py"],
    "backend/app/services": ["auth_service.py", "post_service.py", "group_service.py", "activity_service.py", "book_service.py"],
    "backend/app/db": ["base.py", "session.py", "init_db.py"],
    "backend/app/utils": ["hashing.py", "id_generator.py", "datetime.py"],
    "frontend/components/layout": ["Topbar.tsx", "RightSidebar.tsx"],
    "frontend/styles": ["globals.css"],
    "frontend/lib/api": ["auth.ts", "posts.ts", "books.ts", "groups.ts", "users.ts"]
}

def create_structure():
    for path in BASE_DIRS:
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created: {path}")

    for file_path in FILES_TO_CREATE:
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")
            print(f"📄 Created: {file_path}")

    for folder, files in FOLDER_FILES.items():
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")
                print(f"📄 Created: {file_path}")

if __name__ == "__main__":
    create_structure()
