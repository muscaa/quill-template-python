from pathlib import Path

import scripts

PROJECT_ROOT = Path(scripts.__file__).parent.parent
SRC = PROJECT_ROOT / "src"
SRC_QUILL_HOME = SRC / "_"
SRC_QUILL_PACKAGE = SRC
BUILD = PROJECT_ROOT / "build"
BUILD_GENERATED = BUILD / "generated"
