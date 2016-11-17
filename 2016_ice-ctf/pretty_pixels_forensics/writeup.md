I'm writing this well after the fact. I truly have no idea how I discovered how to solve this. 

This was entirely based off a hunch I suspect. Basically the image is made of a random splatter of pixels which no noticeable pattern and no fixed table of colors.

The most noticeable thing about this image is that the first ~30 pixels are very dark compared to the others. ASCII has low values, this may be a giveaway as the PNG header is in ASCII. 

Basically, take each RGB value of each pixel, which is a byte, and concat them together. Barf that to another file.png and then you have your image.

The reason we cannot see the PNG header in a hex dump of the original is due to the way each pixel is encoded. 