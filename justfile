init:
    python3 -m venv .venv
    ( .venv/bin/pip install --upgrade pip || .venv\Scripts\python.exe -m pip install --upgrade pip )
    ( .venv/bin/pip install -r requirements.txt || .venv\Scripts\pip.exe install -r requirements.txt )
    ( brew install yarn || npm install --global yarn )
    yarn install
    
run-fastapi:
    ( .venv/bin/python -m uvicorn nexus_fastapi.main:app --reload --port 8002 || .venv\Scripts\python.exe -m uvicorn nexus_fastapi.main:app --reload --port 8002 )

run-react:
    yarn workspace nexus-react start

build-docs:
    yarn workspace nexus-react build    

run-docs:
    yarn workspace nexus-docs start

build-docs:
    yarn workspace nexus-docs build