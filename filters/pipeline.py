import os
import cv2
import utils
import filters.grayscale as g
import filters.dilate as d
import filters.blur as b
import logger as log
import filters.filter_ze_team as z

def pipeline_filter (config):
    """
    Apply one or more filters on images from a given directory and saves them to an output directory.

    :param config: A dict that contain an input directory, an output directory and an array of filters
    :return:
    """

    try:
        all_files = utils.get_all_img(config["input"])

        if os.path.exists(config["output"]) == False:
            os.mkdir(config["output"])

        count=1
        lenF = len(all_files)
        for file in all_files:
            try:

                img = cv2.imread(file)
                utils.progress_bar(lenF,count)

                for filter in config["filters"]:

                    if ":" in filter:
                        power = int(filter.split(":")[1])
                        filter = filter.split(":")[0]

                        assert power > 0, f"la taille du {filter} ne peut pas être négatif"
                        assert power % 2 !=0, f"la taille du {filter} ne peut pas être paire"

                    if filter == 'grayscale':
                        img = g.gray_filter(img)
                        log.log(f"Grayscale applied to the following file: {file}")
                    elif filter == 'blur':
                        img = b.blur_filter(img, power)
                        log.log(f"Blur applied to the following file: {file}")
                    elif filter == 'dilate':
                        img = d.dilate_filter(img, power)
                        log.log(f"Dilation applied to the following file: {file}")
                    elif filter == 'zeteam':
                        img = z.ze_team(img)
                        log.log(f"Team member name applied to the following file: {file}")

                cv2.imwrite(f'{config["output"]}/image{count}.png', img)
                count = count +1
            except (cv2.error, AssertionError) as e:
                print(f"Cannot convert this file, error:{e}")
        utils.progress_bar(lenF, count)


    except (FileNotFoundError) as e:
        print(f"Cannot convert image, error:{e}")








