from PIL import Image

img = Image.open('images/logo.png') # image extension *.png,*.jpg
new_width  = 2000
new_height = 300
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('newA.3.png') # format may what u want ,*.png,*jpg,
