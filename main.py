from PIL import Image, ImageFont, ImageDraw
import random
from facts import facts, text_format

Ig = Image.open("graphics/coolbugfacts.png")

IgM = ImageDraw.Draw(Ig)
fnt = ImageFont.truetype("graphics/Roboto-Black.ttf", 25)
i = random.randint(0, len(facts) - 1)
print(i)
txt = text_format(facts[i])
IgM.text((280, 220), txt, fill=(0, 0, 0), font=fnt)

Ig.show()