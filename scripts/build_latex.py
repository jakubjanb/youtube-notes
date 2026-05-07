#!/usr/bin/env python3
"""Compile LaTeX notes into PDFs when local LaTeX tooling is available."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


def find_tex_files(roots: list[str]) -> list[Path]:
    tex_files: list[Path] = []
    for root_text in roots:
        root = Path(root_text)
        if root.is_file() and root.suffix == ".tex":
            tex_files.append(root)
        elif root.exists():
            tex_files.extend(sorted(root.rglob("note.tex")))
    return sorted(set(tex_files))


def build_one(tex_path: Path) -> int:
    if not tex_path.exists():
        print(f"Missing LaTeX file: {tex_path}")
        return 1

    latexmk = shutil.which("latexmk")
    lualatex = shutil.which("lualatex")
    if latexmk:
        command = ["latexmk", "-g", "-lualatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name]
        runs = [command]
    elif lualatex:
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name]
        runs = [command, command]
    else:
        print("No LaTeX compiler found. Install latexmk or lualatex to build PDFs.")
        return 2

    root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    texmf_var = root / "latex" / "builds" / "texmf-var"
    texmf_config = root / "latex" / "builds" / "texmf-config"
    texmf_var.mkdir(parents=True, exist_ok=True)
    texmf_config.mkdir(parents=True, exist_ok=True)
    env.setdefault("TEXMFVAR", str(texmf_var))
    env.setdefault("TEXMFCONFIG", str(texmf_config))

    print(f"Building {tex_path}")
    for command in runs:
        completed = subprocess.run(command, cwd=tex_path.parent, env=env)
        if completed.returncode != 0:
            return completed.returncode
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", nargs="?", help="Path to a .tex file.")
    parser.add_argument("--all", nargs="*", metavar="ROOT", help="Build note.tex files under these roots.")
    args = parser.parse_args()

    if args.all is not None:
        roots = args.all or ["notes"]
        tex_files = find_tex_files(roots)
    elif args.tex:
        tex_files = [Path(args.tex)]
    else:
        parser.error("provide a .tex file or use --all")

    if not tex_files:
        print("No LaTeX files found.")
        return 0

    status = 0
    for tex_path in tex_files:
        status = max(status, build_one(tex_path))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
