#!/bin/sh
echo "🔒 Updating requirements.txt from uv..."
uv pip freeze > requirements.txt
git add requirements.txt
