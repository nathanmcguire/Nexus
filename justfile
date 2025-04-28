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
run-docs:
    .venv\Scripts\mkdocs.exe serve

[macos]
run-docs:
    .venv/bin/mkdocs serve

[windows]
run-docs-no-cache:
    .venv\Scripts\python.exe scripts\set_mkdocs_puml_cache_backend.py disable
    .venv\Scripts\mkdocs.exe serve
    .venv\Scripts\python.exe scripts\set_mkdocs_puml_cache_backend.py enable

[macos]
run-docs-no-cache:
    .venv/bin/python3 scripts/set_mkdocs_puml_cache_backend.py disable
    .venv/bin/mkdocs serve
    .venv/bin/python3 scripts/set_mkdocs_puml_cache_backend.py enable

[windows]
clean-docs:
    if (Test-Path "docs/site/") { Remove-Item -Recurse -Force "docs/site/" }
    .venv\Scripts\mkdocs.exe build --clean
    .venv\Scripts\python.exe scripts\set_mkdocs_puml_cache_backend.py enable


[macos]
clean-docs:
    rm -rf docs/site/
    .venv/bin/mkdocs build --clean
    .venv/bin/python3 scripts/set_mkdocs_puml_cache_backend.py enable

[windows]
run-api:
    $env:PYTHONPATH="${PWD}\nexus_fastapi"; .venv\Scripts\python.exe -m uvicorn nexus_fastapi.main:app --reload --port 8002

[macos]
run-api:
    PYTHONPATH="${PWD}/nexus_fastapi" .venv/bin/python -m uvicorn nexus_fastapi.main:app --reload --port 8002

