from PIL import Image

# Read in an image from a jpg-file and store it in the variable im
im = Image.open("images/image_1.jpg")

# Determine the size of the image
width, height = im.size
print('width: %d, height: %d' % (width, height))

# Convert the image to RGB
rgb_im = im.convert('RGB')

# Determine the rgb values of the pixel at location (row,col) where both row and col are 0
pixel = rgb_im.getpixel((0, 0))
print('Pixel (R, G, B): (%d, %d, %d)' % (pixel[0], pixel[1], pixel[2]))
