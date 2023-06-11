import pyqrcode
from pyqrcode import QRCode

# string to reprsent the qrcode
s = "https://github.com/nig3l"

# generate 
url = pyqrcode.create(s)
url.svg("mygithubprofile.svg", scale = 7)