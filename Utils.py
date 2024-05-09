from PIL import Image
from Matrix import Matrix64
import base64
from io import BytesIO

class Utility:

    def image_to_matrix(self, img_path): #BAD
        img = Image.open(img_path)
        img = img.convert('RGB')
        size = (64, 64)
        print("scaling")
        #scaled = img.resize(size)
        print("scaled")
        matrix = Matrix64(64, 64)
        for row in range(64):
            for col in range(64):
                pixel = img.getpixel((col, row))  # Corrected order (col, row) for getpixel access
                matrix.set_item(row, col, pixel)
        return matrix

    def image_to_base64(self, img):
        img_buffer = BytesIO()
        img.save(img_buffer, format='JPEG')
        byte_data = img_buffer.getvalue()
        base64_str = base64.b64encode(byte_data).decode('utf-8')
        return base64_str