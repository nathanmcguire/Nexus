init:
    python3 -m venv .venv
    ( .venv/bin/pip install --upgrade pip || .venv\Scripts\pip.exe install --upgrade pip )
    ( .venv/bin/pip install -r requirements.txt || .venv\Scripts\pip.exe install -r requirements.txt )
    yarn install