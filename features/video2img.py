import os.path
import cv2
import logger as log


def video2img(video_path, output):
    """
    Extract all frames of a video and convert them into images.

    :param video_path: The location of the video.
    :param output: the output directory for images.
    :return:
    """
    try:
        if os.path.exists(output) == False:
            os.mkdir(output)
        video = cv2.VideoCapture(video_path)
        sucess, image = video.read()
        count = 0
        while sucess:
            cv2.imwrite(f"{output}/{count}_frame.png", image)
            sucess,image = video.read()
            count +=1

        log.log(f"The following video : {video_path} has been converted into frame")
    except (FileNotFoundError, cv2.error) as e:
        print(f"Can't extract frame, error:{e}")