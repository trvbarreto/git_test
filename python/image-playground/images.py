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

converted_img = img.convert('L')
converted_img.save('converted.png', 'png')

# filtered_img.show()
# converted_img.show()

crooked = filtered_img.rotate(180)
crooked.save('upside.png', 'png')

resize = filtered_img.resize((300, 300))
resize.save('resized.png', 'png')

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('croped.png', 'png')
