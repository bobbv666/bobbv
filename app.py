import os
import random
from flask import send_file

# Set the base directory to where this script (app.py) is located
files_directory = os.path.dirname(os.path.abspath(__file__))

def get_random_sanrio_image():
    sanrio_files = os.listdir(os.path.join(files_directory, "sanrio"))
    random_image = random.choice(sanrio_files)
    file_path = os.path.join(files_directory, "sanrio", random_image)
    return send_file(file_path, mimetype='image/png')