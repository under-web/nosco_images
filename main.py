from PIL import Image
from PIL import ImageFilter
import imagehash

img1=Image.open(r"1.jpg")
img2=Image.open(r"1.jpg")

if img1.width<img2.width:
    img2=img2.resize((img1.width,img1.height))
else:
    img1=img1.resize((img2.width,img2.height))

img1=img1.filter(ImageFilter.BoxBlur(radius=3))
img2=img2.filter(ImageFilter.BoxBlur(radius=3))
phashvalue=imagehash.phash(img1)-imagehash.phash(img2)
ahashvalue=imagehash.average_hash(img1)-imagehash.average_hash(img2)
totalaccuracy=phashvalue+ahashvalue

print(totalaccuracy)
print(phashvalue)
print(ahashvalue)