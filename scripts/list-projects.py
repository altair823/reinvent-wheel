#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parent.parent / "topics"
for makefile in sorted(root.glob("*/**/Makefile")):
    print(makefile.parent.relative_to(root.parent))
