#!/usr/bin/env python3
"""Build a clean Product Advisory Board skill ZIP.

This script is maintainer tooling only. Normal users do not need Python.
It packages only the files required by the skill runtime and intentionally
excludes scripts, evals, git metadata, and other development artifacts.
"""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "dist" / "product-advisory-board.zip"


def copy_if_exists(src: Path, dst: Path) -> None:
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    elif src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)


def validate_package(stage: Path) -> None:
    required = [stage / "SKILL.md", stage / "references" / "persona-roster.md"]
    missing = [str(p.relative_to(stage)) for p in required if not p.exists()]
    if missing:
        raise SystemExit(f"Missing required skill files: {', '.join(missing)}")


def build(output: Path) -> Path:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as temp_dir:
        stage = Path(temp_dir) / "product-advisory-board"
        stage.mkdir(parents=True)

        copy_if_exists(ROOT / "SKILL.md", stage / "SKILL.md")
        copy_if_exists(ROOT / "references", stage / "references")
        copy_if_exists(ROOT / "agents", stage / "agents")

        validate_package(stage)

        with ZipFile(output, "w", ZIP_DEFLATED) as zf:
            for path in sorted(stage.rglob("*")):
                if path.is_file():
                    zf.write(path, path.relative_to(stage.parent))

    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the installable skill ZIP")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    built = build(args.output)
    print(f"Built: {built}")


if __name__ == "__main__":
    main()
