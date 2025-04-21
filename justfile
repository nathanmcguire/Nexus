set windows-shell := ["powershell.exe", "-c"]

[windows]
init:
    python3 -m venv .venv
    .venv\Scripts\python.exe -m pip install --upgrade pip
    .venv\Scripts\pip.exe install -r requirements.txt
    brew install yarn
    yarn install

[macos]
init:
    python3 -m venv .venv
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r requirements.txt
    npm install --global yarn
    yarn install

[windows]
run-fastapi:
    $env:PYTHONPATH="${PWD}\nexus_fastapi"; .venv\Scripts\python.exe -m uvicorn nexus_fastapi.main:app --reload --port 8002

[macos]
run-fastapi:
    uvicorn nexus_fastapi.main:app --reload --port 8002

run-react:
    yarn workspace nexus_react start

build-react:
    yarn workspace nexus_react build    


freeze-pip:
    pip freeze > requirements.txt

install-pip PACKAGE:
    pip install {{PACKAGE}}
    pip freeze > requirements.txt

[windows]
init-alembic:
    .venv\Scripts\python.exe -m alembic init alembic

[windows]
migrate-alembic MESSAGE:
    .venv\Scripts\python.exe -m alembic revision --autogenerate -m "{{MESSAGE}}"

[windows]
upgrade-alembic:
    .venv\Scripts\python.exe -m alembic upgrade head