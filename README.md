# ⚔️ Nexus

## Clone This Repo

```bash
git clone https://github.com/nathanmcguire/nexus.git
```


## 🛠 Dependencies

- `python3`  
  - macOS: `brew install python`
  - Windows: [Download from python.org](https://www.python.org/downloads/windows/)

- `node.js`  
  - macOS: `brew install node`
  - Windows: [Download from nodejs.org](https://nodejs.org/)

- `just`  
  - macOS: `yarn add -D just-install`
  - Windows: `yarn add -D just-install`

## 🚀 Automation with justfile

### Initialize the Project
```bash
just init
```
- Creates a virtual environment in `.venv`.
- Upgrades `pip`.
- Installs dependencies from `requirements.txt`.
- Installs `yarn` globally if not already installed.
- Installs JavaScript dependencies using `yarn`.

### Run FastAPI Development Server
```bash
just run-fastapi
```
- Starts the FastAPI server using `uvicorn` with hot-reloading enabled.
- The server will be available at `http://localhost:8002`.

### Run React Development Server
```bash
just run-react
```
- Starts the React development server for the `nexus-react` workspace.
- The server will be available at `http://localhost:8001`.

### Run Documentation Development Server
```bash
just run-docs
```
- Starts the documentation server using Docusaurus.
- The documentation will be available at `http://localhost:8003`