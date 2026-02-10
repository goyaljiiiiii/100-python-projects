#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECTS_DIR = ROOT / "projects"
PROJECTS_INDEX = ROOT / "PROJECTS.md"


def _load_index_names():
    names = {}
    if not PROJECTS_INDEX.exists():
        return names
    for line in PROJECTS_INDEX.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4 or parts[0].lower() == "#":
            continue
        num = parts[0]
        name = parts[1]
        path = parts[2].strip("`")
        names[num] = {"name": name, "path": path}
    return names


def _discover_projects():
    projects = []
    for p in sorted(PROJECTS_DIR.iterdir()):
        if not p.is_dir() or p.name.startswith("_"):
            continue
        main_py = p / "main.py"
        if not main_py.exists():
            continue
        # Numeric folder like 001 or 012
        m = re.match(r"^(\d+)", p.name)
        if not m:
            continue
        num = m.group(1)
        projects.append({"num": num, "dir": p, "main": main_py})
    return projects


def _run_project(main_path: Path):
    try:
        subprocess.run([sys.executable, str(main_path)], check=False)
    except KeyboardInterrupt:
        print("\nProject interrupted. Returning to launcher...")
    finally:
        input("\nPress Enter to return to the launcher...")


def main():
    names = _load_index_names()
    projects = _discover_projects()
    if not projects:
        print("No projects found in projects/.")
        return

    while True:
        print("\n=== 100 Python Projects Launcher ===")
        print("Type a project number (001-100) or q to quit.")
        choice = input("Run project: ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            print("Goodbye!")
            return

        # normalize choice (allow 1 -> 001 if exists)
        match = None
        normalized = choice.zfill(3) if choice.isdigit() else choice
        for proj in projects:
            if normalized == proj["num"]:
                match = proj
                break

        if not match:
            print("Project not found. Try another number.")
            continue
        num = match["num"]
        name = names.get(num, {}).get("name", f"Project {num}")
        print(f"\nRunning {num} - {name}...\n")
        _run_project(match["main"])


if __name__ == "__main__":
    main()
