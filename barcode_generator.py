from barcode import EAN13
from barcode.writer import ImageWriter

number = "123456789101112"

barcode  = EAN13(number,writer=ImageWriter())

barcode.save("barcode")
print("barcode")