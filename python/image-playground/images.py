from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
# img.format
# img.size
# img.mode

filtered_img = img.filter(ImageFilter.SHARPEN)
# ImageFilter.BLUR
# ImageFilter.SMOOTH
# ImageFilter.SHARPEN
filtered_img.save('filtered.png', 'png')

coverted_img = img.convert('L')
coverted_img.save('converted.png', 'png')
