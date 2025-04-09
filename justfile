set windows-shell := ["powershell.exe", "-c"]

init:
    python3 -m venv .venv
    if (Test-Path .venv\Scripts\pip.exe) { .venv\Scripts\python.exe -m pip install --upgrade pip; .venv\Scripts\pip.exe install -r requirements.txt } else { .venv/bin/pip install --upgrade pip; .venv/bin/pip install -r requirements.txt }
    if (Get-Command brew -ErrorAction SilentlyContinue) { brew install yarn } else { npm install --global yarn }
    yarn install

    
run-fastapi:
    if (Test-Path .venv\Scripts\python.exe) { .venv\Scripts\python.exe -m uvicorn nexus-fastapi:app --reload --port 8002 } else { .venv/bin/python -m uvicorn nexus-fastapi:app --reload --port 8002 }

run-react:
    yarn workspace nexus-react start

build-react:
    yarn workspace nexus-react build    

run-docs:
    yarn workspace nexus-docs start

build-docs:
    yarn workspace nexus-docs build

version-docs VERSION:
    yarn workspace nexus-docs run docusaurus docs:version {{VERSION}}