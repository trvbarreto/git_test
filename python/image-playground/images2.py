from PIL import Image

img = Image.open('./deer.jpg')
print(img.size)
new_img = img.resize((400, 400))
new_img.save('deer-resized.png', 'png')
new_img.save('deer-resized2.png', 'png')

deer = Image.open('./deer.jpg')
deer.thumbnail((400, 400))
deer.save('thumbnail.png')

print(new_img.size)
print(deer.size)

# Thumbnail tries to resize the best way possible within the passed tuple (400,400)
