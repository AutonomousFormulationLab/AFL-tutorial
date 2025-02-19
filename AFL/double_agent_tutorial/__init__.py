from AFL.double_agent_tutorial.core import *
import pathlib

# Get the package install directory
PACKAGE_DIR = pathlib.Path(__file__).parent.parent.parent.resolve()
DATA_DIR = PACKAGE_DIR / "data"

print(PACKAGE_DIR)
print(DATA_DIR)