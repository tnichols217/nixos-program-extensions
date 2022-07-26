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
    return ext + ".zip"

def downloadLink(ext):
    os.system("curl -L " + getDownloadLink(ext) + " -o out/" + filename(ext))

pathlib.Path("./out").mkdir(exist_ok=True)
[path.unlink() for path in pathlib.Path("./out").glob("*")]
[downloadLink(link) for link in exts]