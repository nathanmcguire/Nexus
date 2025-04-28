set windows-shell := ["powershell.exe", "-c"]

[windows]
init:
    if (-Not (Test-Path ".venv")) { python -m venv .venv }
    .venv\Scripts\python.exe -m pip install --upgrade pip
    .venv\Scripts\pip.exe install -r requirements-dev.txt
    #brew install yarn
    #yarn install

[macos]
init:
    if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r requirements-dev.txt
    #npm install --global yarn
    #yarn install

[windows]
activate:
    echo ".venv\Scripts\activate.ps1"

[macos]
activate:
    echo "source .venv/bin/activate"

run-react:
    yarn workspace nexus_react start

build-react:
    yarn workspace nexus_react build

[windows]
init-alembic:
    .venv\Scripts\python.exe -m alembic init alembic

[windows]
migrate-alembic MESSAGE:
    .venv\Scripts\python.exe -m alembic revision --autogenerate -m "{{MESSAGE}}"

[windows]
upgrade-alembic:
    .venv\Scripts\python.exe -m alembic upgrade head

[windows]
serve-docs:
    .venv\Scripts\mkdocs.exe serve

[macos]
serve-docs:
    .venv/bin/mkdocs serve

[windows]
clean-docs:
    if (Test-Path "docs/site/") { Remove-Item -Recurse -Force "docs/site/" }
    if (Test-Path "$env:USERPROFILE/.cache/mkdocs_puml/nexus") { Remove-Item -Recurse -Force "$env:USERPROFILE/.cache/mkdocs_puml/nexus" }
    .venv\Scripts\mkdocs.exe build --clean

[macos]
clean-docs:
    rm -rf docs/site/
    rm -rf ~/.cache/mkdocs_puml/nexus
    .venv/bin/mkdocs build --clean

[windows]
serve-api:
    $env:PYTHONPATH="${PWD}\nexus_fastapi"; .venv\Scripts\python.exe -m uvicorn nexus_fastapi.main:app --reload --port 8002

[macos]
serve-api:
    PYTHONPATH="${PWD}/nexus_fastapi" .venv/bin/python -m uvicorn nexus_fastapi.main:app --reload --port 8002

