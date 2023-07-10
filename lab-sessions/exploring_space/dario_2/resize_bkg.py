from PIL import Image

img = Image.open("background.png")

new_width = 1500
new_height = 1500

resized_img = img.resize((new_width, new_height))

resized_img.save("bkg.png")