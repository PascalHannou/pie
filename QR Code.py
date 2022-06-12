import pyqrcode
import png
from pyqrcode import QRCode

# String which represent the QR code
s = "https://medium.com/@pascal.h"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming 
url.svg("myblog.svg", scale = 10)

# Create and save the png file naming 
url.png ("myblog.png", scale = 8)
