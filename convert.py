import os
from PIL import Image

# Batch Image Format Converter

input_folder = "path_to_input_folder"  # Replace with your input folder path
output_folder = "path_to_output_folder"  # Replace with your output folder path
input_format = ".webp"  # Replace with the input file format (e.g., ".png", ".webp")
output_format = ".jpg"  # Replace with the output file format (e.g., ".png", ".jpg")

# Create Output Folder if Not Exists
os.makedirs(output_folder, exist_ok=True)

# Convert Files

for filename in os.listdir(input_folder):
    if filename.endswith(input_format):  # Check if the file matches the input format
        input_path = os.path.join(input_folder, filename)  # Full path to the input file
        output_filename = f"{os.path.splitext(filename)[0]}{output_format}"  # Set output filename
        output_path = os.path.join(output_folder, output_filename)  # Full path to the output file

        with Image.open(input_path) as img:
            # Convert the image and save it in the desired format
            img.convert("RGB").save(output_path, output_format.strip(".").upper())  
            print(f"Converted: {filename} to {output_format}")


