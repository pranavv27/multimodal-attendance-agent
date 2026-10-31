import sys
from pathlib import Path

# Ensure backend package and its internal modules are importable
ROOT = Path(__file__).resolve().parent.parent
BACKEND = ROOT / "backend"
for path in (str(ROOT), str(BACKEND)):
    if path not in sys.path:
        sys.path.insert(0, path)

# Single ASGI application entrypoint for Vercel
from backend.main import app  # noqa: E402,F401,E501
