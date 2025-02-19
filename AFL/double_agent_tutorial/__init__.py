from AFL.double_agent_tutorial.core import *
import pathlib

# Get the package install directory
PACKAGE_DIR = pathlib.Path(__file__).parent.parent.parent.resolve()
DATA_DIR = PACKAGE_DIR / "data"

print(f"PACKAGE_DIR: {PACKAGE_DIR}")
print(f"DATA_DIR: {DATA_DIR}")