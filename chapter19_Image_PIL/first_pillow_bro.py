from PIL import ImageColor, Image

# print(ImageColor.getcolor("red", "RGBA"))

cat = Image.open("zophie.png")
print(type(cat))
print(cat.size)
print(cat.width)
print(cat.height)
print(cat.format)
print(cat.filename)
print(cat.format_description)
# cat.save("zophie.jpg")

im = Image.new("RGBA", (100, 200), "purple")
im.save("purpleImage.png")
