import os
import random
from flask import Flask, send_file

# Initialize the Flask application
app = Flask(__name__)

# Set the base directory to where this script (app.py) is located
files_directory = os.path.dirname(os.path.abspath(__file__))

@app.route('/random_image')
def get_random_sanrio_image():
    # Get the list of image files in the 'sanrio' folder
    sanrio_files = os.listdir(os.path.join(files_directory, "sanrio"))
    
    # Choose a random image
    random_image = random.choice(sanrio_files)
    
    # Get the full file path
    file_path = os.path.join(files_directory, "sanrio", random_image)
    
    # Return the image as a response
    return send_file(file_path, mimetype='image/png')

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
