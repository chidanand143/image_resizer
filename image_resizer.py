import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, size=(128, 128)):
    """
    Resizes all image files in the input_folder and saves them to the output_folder.

    Args:
        input_folder (str): The directory containing the original images.
        output_folder (str): The directory to save the resized images.
        size (tuple): The target size (width, height) for the images.
    """
    # 1. Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # 2. Iterate through all files in the input folder
    print(f"Starting image resizing from {input_folder}...")
    for filename in os.listdir(input_folder):
        # Construct the full file path
        input_path = os.path.join(input_folder, filename)

        # Check if the path is a file and not a folder
        if os.path.isfile(input_path):
            try:
                # 3. Use PIL.Image to open the image
                img = Image.open(input_path)
                
                # Resize the image (using thumbnail to maintain aspect ratio, 
                # or use .resize() for exact dimension)
                # Using .resize() for the exact requested dimensions:
                resized_img = img.resize(size) 

                # Construct the output path
                # We save the resized image with a prefix for clarity
                name, ext = os.path.splitext(filename)
                output_filename = f"{name}_resized{ext}"
                output_path = os.path.join(output_folder, output_filename)

                # Save the resized image
                resized_img.save(output_path)
                print(f"Successfully resized and saved: {filename} -> {output_filename}")

            except IOError:
                # Handle cases where the file is not a valid image
                print(f"Warning: Could not open or process file {filename}. Skipping.")
            except Exception as e:
                # Catch any other potential errors
                print(f"An error occurred while processing {filename}: {e}")

    print("---")
    print("Batch image resizing complete!")

# --- Configuration ---
# You need to create an 'input_images' folder and put your images inside it
INPUT_DIR = 'input_images'
OUTPUT_DIR = 'output_resized'
TARGET_SIZE = (300, 200) # Example size: 300 pixels wide by 200 pixels high

# --- Execution ---
if __name__ == '__main__':
    # 🚨 IMPORTANT: Before running, create a folder named 'input_images' 
    # in the same directory as this script and place your images inside it.
    
    # You can optionally create dummy folders for testing if they don't exist
    if not os.path.exists(INPUT_DIR):
        print(f"*Action Required*: Please create a folder named '{INPUT_DIR}' and place your test images inside.")
    else:
        resize_images_in_folder(INPUT_DIR, OUTPUT_DIR, TARGET_SIZE)