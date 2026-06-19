import zipfile

import __about__ as a
from scripts.files import SRC, BUILD, BUILD_GENERATED
from scripts import generate

def run():
    generate()

    BUILD.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(BUILD / f"{a.ID}-bundle.zip", "w", zipfile.ZIP_DEFLATED) as zip:
        for f in SRC.rglob("*"):
            if f.is_file():
                zip.write(f, f.relative_to(SRC))
        for f in BUILD_GENERATED.rglob("*"):
            if f.is_file():
                zip.write(f, f.relative_to(BUILD_GENERATED))
