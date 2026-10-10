"""Run every numbered example in order."""

import subprocess
import sys
from pathlib import Path

here = Path(__file__).parent
for script in sorted(here.glob("[0-9][0-9]_*.py")):
    print(f"\n{'#' * 70}\n# {script.name}\n{'#' * 70}")
    subprocess.run([sys.executable, str(script)], cwd=here)
