# ⚔️ Nexus

## 🛠 Dependencies

- `python3`  
  - macOS: `brew install python`
  - Windows: [Download from python.org](https://www.python.org/downloads/windows/)

- `node.js`  
  - macOS: `brew install node`
  - Windows: [Download from nodejs.org](https://nodejs.org/)

- `yarn`  
  - macOS: `brew install yarn`
  - Windows: `npm install --global yarn`

- `just`  
  - macOS: `brew install just`
  - Windows: `choco install just` or [Download from GitHub](https://github.com/casey/just/releases)

## Clone This Repo

```bash
git clone https://github.com/nathanmcguire/nexus.git
```

## 🚀 Run justfile
```bash
just init
```
- Create a virtual environment in `.venv`
- Upgrade `pip`
- Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Backend FastAPI

### Activate the Virtual Environment
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

### Run the Development Server
```bash
uvicorn nexus-fastapi.main:app --reload
```
port 8000

## Nexus React (Frontend)
```bash
yarn workspace nexus-react start
```
port 3000

## Docs
```bash
yarn workspace docs start
```
port 4000
