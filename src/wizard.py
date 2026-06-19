from quill.setup.versions import V1

def install():
    v1 = V1(__file__)
    v1.copy("wizard.py")
    v1.copy("package.json")

    v1.bins([
        "_/bin/quill-template-python",
        "_/bin/quill-template-python.cmd",
    ])

    v1.copy("bin/")
    v1.copy("quill/")

def uninstall():
    v1 = V1(__file__)
    v1.delete("wizard.py")
    v1.delete("package.json")

    v1.delete("@/bin/quill-template-python")
    v1.delete("@/bin/quill-template-python.cmd")

    v1.delete("bin/")
    v1.delete("quill/")
