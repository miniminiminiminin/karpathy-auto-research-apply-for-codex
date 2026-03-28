from __future__ import annotations

import argparse
import sys
from pathlib import Path


SDK_SRC = Path(__file__).resolve().parent / "codex_writer_sdk" / "src"
if str(SDK_SRC) not in sys.path:
    sys.path.insert(0, str(SDK_SRC))

from codex_writer.workspace.init import initialize_workspace  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--preset", default="book-chapter")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    initialize_workspace(Path(args.workspace), args.preset)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
