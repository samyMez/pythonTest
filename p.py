import math
import sys
from os import rename

import requests

r = requests.get("https://coreyms.com")
print(r.status_code, "lol")
print(sys.version)


def samyo(chiffre):
    if chiffre >= 0:
        return chiffre + 5
    else:
        pass


sam = samyo(5)
print(sam, "yoooooooooooooGlooooooooo")
