import os
from PIL import Image

# pip install pillow
# Input and output folder paths
input_folder = "input folder location"
output_folder = "output folder location"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".webp"):
        webp_path = os.path.join(input_folder, filename)
        jpg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
        with Image.open(webp_path) as img:
            img.convert("RGB").save(jpg_path, "JPEG")
        print(f"Converted: {filename} to JPG")
