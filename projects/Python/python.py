from pathlib import Path

# ======================================================
# GitHub Portfolio Structure
# Author: Marcelly Maia
# ======================================================

ROOT = Path("MarcellyMaia")

folders = [

    # Assets
    "assets/banners",
    "assets/icons",
    "assets/logos",
    "assets/backgrounds",
    "assets/profile",
    "assets/social",

    # Images
    "images/github",
    "images/linkedin",
    "images/medium",
    "images/certificates",
    "images/projects",
    "images/screenshots",

    # Documentation
    "docs/resume",
    "docs/certifications",
    "docs/roadmap",
    "docs/media-kit",

    # Projects
    "projects/PowerBI",
    "projects/PowerAutomate",
    "projects/PowerApps",
    "projects/Python",
    "projects/SQL",
    "projects/Excel",
    "projects/SharePoint",
    "projects/DataEngineering",

    # Articles
    "articles/medium",
    "articles/linkedin",
    "articles/english",

    # Templates
    "templates/README",
    "templates/Issues",
    "templates/License",

    # GitHub
    ".github/workflows",
    ".github/ISSUE_TEMPLATE",
    ".github/PULL_REQUEST_TEMPLATE",
]

# Criar pastas
for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)

# Arquivos principais
files = [
    "README.md",
    "LICENSE",
    ".gitignore",
]

for file in files:
    file_path = ROOT / file
    file_path.touch(exist_ok=True)

print("=" * 50)
print("✅ Estrutura criada com sucesso!")
print(f"📁 Pasta principal: {ROOT.resolve()}")
print("=" * 50)

# Mostrar estrutura criada
for path in sorted(ROOT.rglob("*")):
    level = len(path.relative_to(ROOT).parts)
    indent = "    " * (level - 1)
    icon = "📁" if path.is_dir() else "📄"
    print(f"{indent}{icon} {path.name}")