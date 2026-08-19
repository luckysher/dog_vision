from PIL import Image
import os
from pathlib import Path



def resize_images(path, img_height, img_width):
    # for all folders

    processed_files_dir = "processed"
    # create processed folder
    if len(os.listdir(path)) > 0 and not os.path.exists(os.path.join(os.getcwd(), processed_files_dir)):
        os.mkdir(os.path.join(os.getcwd(), processed_files_dir))

    for data_sub_dir in os.listdir(path):
        processed_file_save_path = os.path.join(os.getcwd(), processed_files_dir, data_sub_dir)
        if not os.path.exists(processed_file_save_path):
            os.mkdir(processed_file_save_path)
