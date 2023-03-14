import PIL
from PIL import ImageDraw
#im = PIL.Image.open(r"C:/Users/Utente03/Pictures/IMG-20210703-WA0013.jpg")
im = PIL.Image.open(r"C:/Users/Utente03/Pictures/IMG_20210715_113530.jpg")
im.show()

# Create a reader to do OCR.
# If you change to GPU instance, it will be faster. But CPU is enough.
# (by MENU > Runtime > Change runtime type > GPU, then redo from beginning )
import easyocr
reader = easyocr.Reader(['it','en'])
bounds = reader.readtext(r"C:/Users/Utente03/Pictures/IMG_20210715_113530.jpg")
#bounds = reader.readtext(r"C:/Users/Utente03/Pictures/IMG-20210703-WA0013.jpg")
print(bounds)
print("type",type(bounds))
print(len(bounds))
print(bounds[11])
print(bounds[11][1])
if len(bounds[11][1])==16:
    print("got C.F:=",bounds[11][1])