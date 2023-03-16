import os

from config import Configuration

conf = Configuration()


def list_images():
    """Returns the list of available images."""
    img_names = filter(lambda x: x.lower().endswith(tuple(conf.IMAGE_FORMATS)),
                       os.listdir(conf.image_folder_path))
    return list(img_names)
