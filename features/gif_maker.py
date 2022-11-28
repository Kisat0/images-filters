from PIL import Image
import os
import logger as log

def image2gif(input_dir, output_dir):
    """
    Convert images into a gif.

    :param input_dir: input directory of the images
    :param output_dir: output directory for the gif
    :return:
    """
    try:
        if os.path.exists(output_dir) == False:
            os.mkdir(output_dir)

        images = os.listdir(input_dir)
        palette_images = []
        for image in images:
            with Image.open(input_dir+image) as img:
                palette_img = img.convert("P")
                palette_images.append(palette_img)

        palette_images[0].save(f"{output_dir}/ultimate.gif",save_all=True,optimize=False, append_images=palette_images[1:], duration=200, loop=0)
        log.log(f"A gif has been created at the following directory : {output_dir}")

    except (FileNotFoundError) as e:
        print(f"Can't convert images into gif, error:{e}")

