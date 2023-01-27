import os
import pathlib
import requests
import re

# extensions.conf can be generated with `code --list-extensions`
with open("./extensions.conf", "r") as f:
    exts = f.read().split("\n")

def getStoreLink(ext):
    return "https://addons.mozilla.org/en-US/firefox/addon/" + ext + "/"

def getDownloadLink(ext):
    storeLink = getStoreLink(ext)
    ret = requests.get(storeLink).text
    link = re.findall(r'https://addons.mozilla.org/firefox/downloads/file/[^"]*', ret)
    return link[0]

def filename(ext):
    return ext + ".xpi"

def downloadLink(ext):
    os.system("curl -L " + getDownloadLink(ext) + " -o out/" + filename(ext))

def generateTarChunks():
    os.system("rm -f out.tar")
    os.system("tar -cf out.tar out")
    pathlib.Path("./chunks").mkdir(exist_ok=True)
    os.system("rm -f chunks/*")
    os.system("split -b 50M out.tar chunks/out.tar.")
    os.system("rm -f out.tar")

pathlib.Path("./out").mkdir(exist_ok=True)
[path.unlink() for path in pathlib.Path("./out").glob("*")]
[downloadLink(link) for link in exts]
generateTarChunks()

[path.unlink() for path in pathlib.Path("./out").glob("*")]