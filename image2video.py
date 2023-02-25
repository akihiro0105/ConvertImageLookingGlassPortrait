import sys
import os
from PIL import Image
from multiprocessing import Process
import subprocess
import shutil
import concat_side

move_time = 10
fps = 60

def process_image(i, out_dir_path, image):
    print("\r", str(i)+"/"+str(move_time*fps), end="")
    target = Image.new('RGB', (1536*2, 2048))
    if (image.width/2) > image.height:
        tmp = image.resize((int((2048/(image.height))*image.width), 2048))
        delta = (tmp.width/2)-1536
        move = int((float(delta)/(move_time*fps))*i)
        target.paste(tmp.crop((move, 0, 1536+move, 2048)), (0, 0))
        target.paste(tmp.crop((move+(tmp.width/2), 0, move +
                     1536+(tmp.width/2), 2048)), (1536, 0))
    else:
        tmp = image.resize((1536*2, int((1536/(image.width/2))*image.height)))
        delta = tmp.height-2048
        move = int((float(delta)/(move_time*fps))*i)
        target.paste(tmp, (0, -move))
    target.save(out_dir_path+"\{:0>4}".format(i)+".png")

if __name__ == '__main__':
    image_path=sys.argv[0]
    if len(sys.argv)==3:
        image_path=concat_side.concat_side(sys.argv[1], sys.argv[2])
    elif len(sys.argv)==2:
        image_path=sys.argv[1]
    else:
        print("set image file path")
        exit()
        
    out_dir_path = os.path.splitext(os.path.basename(image_path))[0]
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("out", exist_ok=True)
    image = Image.open(image_path)
    processes = [Process(target=process_image, args=(
        i, "tmp", image)) for i in range(move_time*fps)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    subprocess.run("ffmpeg -r 60 -i tmp/%04d.png -vcodec libx264 -pix_fmt yuv420p -r 60 out/"+out_dir_path+".mp4")
    shutil.rmtree("tmp")