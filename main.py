from PIL import Image
import colorsys

# グレースケールの画像データを作成
img = Image.new("RGB", (256, 256), (255, 255, 255))
size = img.size

for x in range(size[0]):
    for y in range(size[1]):
        (r, g, b) = colorsys.hsv_to_rgb(212 / 360, x / 255, (255 - y) / 255)
        img.putpixel((x, y), (int(r * 256), int(g * 256), int(b * 256)))

# 画像の表示
img.save('./result/color.png')

