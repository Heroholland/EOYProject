from PIL import Image
from Matrix import Matrix64

class Utility:

    def image_to_matrix(self, img_path):
        img = Image.open(img_path)
        size = (64,64)
        print("scaling")
        scaled = img.resize(size)
        print("scaled")
        matrix = Matrix64(64, 64)
        for row in range(64):
            for col in range(64):
                pixel = scaled.getpixel((row, col))
                matrix.set_item(row, col, pixel)
        return matrix