import os
from PIL import Image

def convert_tif_to_jpeg(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".tif"):
            file_path = os.path.join(folder_path, filename)
            output_filename = os.path.splitext(filename)[0] + ".jpeg"
            output_path = os.path.join(folder_path, output_filename)
            
            # Open and convert the image
            image = Image.open(file_path)
            image = image.convert("RGB")
            
            # Save the converted image as JPEG and replace the original file
            image.save(output_path, "JPEG")
            os.remove(file_path)
            
            print(f"Converted: {filename} -> {output_filename}")

# Provide the folder path where your TIFF files are located
folder_path = ''

# Call the function to convert TIFF files to JPEG
convert_tif_to_jpeg(folder_path)

