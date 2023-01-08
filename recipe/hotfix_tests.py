import site
import shutil
from pathlib import Path

shutil.copytree(
    "src/smart_open/tests",
    Path(site.getsitepackages()[0]) / "smart_open/tests"
)
