from PIL import Image

# h = 1080 + 255
# w = 25
# img = Image.new("RGBA", (w, h))

# for y in range(h):
#     print(f"Generating barfadeRed.png: {y}/{h}", end="\r")
#     for x in range(w):
#         img.putpixel((x, h-y-1), (255, 64, 96, min(y,255)))

# img.save("barfadeRed.png")

# for y in range(h):
#     print(f"Generating barfadeGreen.png: {y}/{h}", end="\r")
#     for x in range(w):
#         img.putpixel((x, h-y-1), (98, 180, 85, min(y,255)))

# img.save("barfadeGreen.png")


h = 50
w = 1185
img = Image.new("RGBA", (w, h))

for y in range(h):
    print(f"Generating choice_hover_background.png: {y}/{h}", end="\r")
    for x in range(w):
        a = min(x, w-x, 255)
        img.putpixel((x, h-y-1), (130, 189, 127, a))

img.save("choice_hover_background.png")