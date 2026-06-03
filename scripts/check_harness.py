#!/usr/bin/env python3
"""Run local harness checks for this repository."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WINDOWS_VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
POSIX_VENV_PYTHON = ROOT / ".venv" / "bin" / "python"


def project_python() -> str:
    if WINDOWS_VENV_PYTHON.exists():
        return str(WINDOWS_VENV_PYTHON)
    if POSIX_VENV_PYTHON.exists():
        return str(POSIX_VENV_PYTHON)
    return sys.executable


def run(command: list[str]) -> None:
    print("Running:", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    python = project_python()
    run([python, "scripts/check_docs_drift.py"])
    run([python, "scripts/check_structure.py"])
    run([python, "scripts/check_encoding_hygiene.py"])
    run([python, "scripts/check_effectiveness_plan.py", "--require-report"])
    run([python, "scripts/check_failure_memory.py"])
    run([python, "scripts/check_decision_memory.py"])

    manage_py = ROOT / "manage.py"
    if manage_py.exists():
        run([python, "manage.py", "check"])
        run([python, "manage.py", "test"])
    else:
        print("Skipping Django checks because manage.py is not present yet.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
