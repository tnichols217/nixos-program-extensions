import os
import pathlib

# extensions.conf can be generated with `code --list-extensions`
with open("./extensions.conf", "r") as f:
    s = f.read()
    i = [j for j in s.split("\n")]

exts = [j.split(".") for j in i]

def filename(ext):
    return ext[0] + "." + ext[1] + ".zip"

def extLink(ext):
    return "https://" + ext[0] + ".gallery.vsassets.io/_apis/public/gallery/publisher/" + ext[0] + "/extension/" + ext[1] + "/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage"

def downloadLink(ext):
    os.system("curl -L " + extLink(ext) + " -o out/" + filename(ext))

def generateTarChunks():
    os.system("rm out.tar")
    os.system("tar -cf out.tar out")
    pathlib.Path("./chunks").mkdir(exist_ok=True)
    os.system("rm chunks/*")
    os.system("split -b 50M out.tar chunks/out.tar.")
    os.system("rm out.tar")

pathlib.Path("./out").mkdir(exist_ok=True)
[path.unlink() for path in pathlib.Path("./out").glob("*")]
[downloadLink(link) for link in exts]
generateTarChunks()

[path.unlink() for path in pathlib.Path("./out").glob("*")]