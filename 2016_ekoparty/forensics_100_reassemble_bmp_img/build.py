import struct
from PIL import Image

# thanks wiki https://en.wikipedia.org/wiki/BMP_file_format
# example was most helpful

f = open("damaged_image.bmp", "rb")

## Read this screwed up header for what we need
f.read(4) # toss
width = struct.unpack('<i', f.read(4))[0]
height = struct.unpack('<i', f.read(4))[0]
f.read(2) # plane
bitsPerPixel = struct.unpack('<h', f.read(2))[0]
f.read(4)
size = struct.unpack('<i', f.read(4))[0]
f.read(16)

rowSize = int((bitsPerPixel * width + 31)/32) * 4

# Rest of file is image data
data = f.read()
f.close()

image = Image.frombytes(
    "RGB", (width, height), data, "raw",
    "BGR", rowSize, -1
    )

image.show()
