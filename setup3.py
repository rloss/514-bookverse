import os

TEMPLATE_CONTENTS = {
    "backend/app/main.py": """from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/\")\ndef root():\n    return {\"message\": \"Welcome to Bookverse API\"}\n""",

    "backend/app/core/config.py": """import os\nfrom pydantic import BaseSettings\n\nclass Settings(BaseSettings):\n    API_V1_STR: str = \"/api/v1\"\n    PROJECT_NAME: str = \"Bookverse\"\n    DATABASE_URL: str = os.getenv(\"DATABASE_URL\")\n\nsettings = Settings()\n""",

    "backend/app/models/base.py": """from sqlalchemy.ext.declarative import as_declarative\n\n@as_declarative()\nclass Base: \n    pass\n""",

    "backend/app/schemas/user.py": """from pydantic import BaseModel\n\nclass UserBase(BaseModel):\n    username: str\n    email: str\n""",

    "backend/app/api/v1/auth.py": """from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get(\"/auth/test\")\ndef test_auth():\n    return {\"msg\": \"Auth router working\"}\n""",

    "frontend/app/layout.tsx": """export default function Layout({ children }: { children: React.ReactNode }) {\n  return (\n    <html lang=\"ko\">\n      <body>{children}</body>\n    </html>\n  );\n}\n""",

    "frontend/app/page.tsx": """export default function Home() {\n  return (\n    <div className=\"p-4\">\n      <h1 className=\"text-2xl font-bold\">📚 Bookverse에 오신 것을 환영합니다</h1>\n    </div>\n  );\n}\n""",

    "frontend/components/layout/Topbar.tsx": """export default function Topbar() {\n  return (\n    <header className=\"w-full h-16 bg-white border-b px-6 flex items-center\">\n      <h1 className=\"text-xl font-bold\">Bookverse</h1>\n    </header>\n  );\n}\n""",

    "frontend/styles/globals.css": """@tailwind base;\n@tailwind components;\n@tailwind utilities;\n\nbody {\n  @apply bg-gray-50 text-gray-800;\n}\n""",

    "frontend/lib/api/auth.ts": """import axios from 'axios';\n\nexport const login = async (providerToken: string) => {\n  return axios.post('/api/v1/auth/social-login', { token: providerToken });\n};\n"""
}

def write_templates():
    for path, content in TEMPLATE_CONTENTS.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
            print(f"📝 Wrote template: {path}")

if __name__ == "__main__":
    write_templates()