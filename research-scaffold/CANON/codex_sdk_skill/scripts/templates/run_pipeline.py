from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SDK_SRC = ROOT / "sdk" / "src"
if str(SDK_SRC) not in sys.path:
    sys.path.insert(0, str(SDK_SRC))

from codex_writer.cli.main import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main(["pipeline", "run", *sys.argv[1:]]))
