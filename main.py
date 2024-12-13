import barcode
from barcode.writer import ImageWriter
from IPython.display import Image,display

def generate_barcode(data):
    code =barcode.get('code128', data, writer= ImageWriter())
    barcode_filename = code.save("barcode")
    print("Barcode generated.")
    
    display(Image(f"{barcode_filename}"))

data = "1234-5678-9052"
generate_barcode(data)