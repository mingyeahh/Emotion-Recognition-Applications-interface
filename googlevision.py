from dotenv import load_dotenv
import io
from pathlib import Path
from google.cloud import vision
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

# Code structure from : https://cloud.google.com/vision/docs/detect-labels-image-client-libraries
# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = Path(args.file)

# Make sure the file exists
assert file_name.is_file()

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.face_detection(image=image, max_results=5)
faces = response.face_annotations

print('Faces:')
for face in faces:
    print(face)
