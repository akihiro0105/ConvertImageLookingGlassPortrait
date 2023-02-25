import sys
import os
from PIL import Image

def concat_side(image_path, depth_path):
    os.makedirs("out", exist_ok=True)
    out_path = "out/"+os.path.splitext(os.path.basename(image_path))[0]+"_concat.png"
    image = Image.open(image_path).convert('RGB')
    depth = Image.open(depth_path).convert('RGB')
    concat_image = Image.new('RGB', (image.width+depth.width, image.height))
    concat_image.paste(image, (0, 0))
    concat_image.paste(depth, (image.width, 0))
    concat_image.save(out_path, "png")
    return out_path

if __name__ == '__main__':
    concat_side(sys.argv[1], sys.argv[2])