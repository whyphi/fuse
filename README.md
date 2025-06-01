Unlike Zap, in this repo, we'll be using uv as our Python package and project manager.

To install uv: https://docs.astral.sh/uv/#installation

To create a virtual environment:

```bash
uv venv
```

To activate the virtual environment:

```bash
source .venv/bin/activate
```

IMPORTANT: To setup pre-commit (https://pre-commit.com/):

```bash
pip install pre-commit
pre-commit install
```

Sync project's dependencies with the environment:
```bash
uv sync
```

To run the server:

```bash
uv run fastapi dev
```