from PIL import Image
overlay = Image.open("contour/contourpeople2.png")
background = Image.open("output/final output/output-people2.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("newpeople2.png","PNG")