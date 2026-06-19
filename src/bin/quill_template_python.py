from quill.package import Package
from quill.template.internal import some_internal_function

def main(package: Package, args: list[str]):
    print("Hello from main package command")
    some_internal_function()
