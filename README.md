# Fuse

### 🛠 Setup Instructions

This repo uses [`uv`](https://docs.astral.sh/uv) as the Python package and project manager (unlike Zap, which used pip/pipenv).

#### Install `uv`
Follow the instructions here: https://docs.astral.sh/uv/#installation

#### Create & activate a virtual environment

```bash
uv venv
```

To activate the virtual environment:

```bash
source .venv/bin/activate
```

#### Sync dependencies

```bash
uv sync
```
This installs everything listed in `pyproject.toml`.

#### Setup pre-commit hooks

Refer to https://pre-commit.com/

```bash
pip install pre-commit
pre-commit install
```

💡 This ensures that `requirements.txt` stays in sync and formatting rules (if any) are enforced.

#### Run the server

```bash
uv run fastapi dev
```