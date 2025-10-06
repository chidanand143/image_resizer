**🖼 Python Image Resizer Tool**

🎯 Objective
This script provides a simple, automated solution for resizing and converting a batch of images within a specified folder. It's built using Python and the Pillow library, allowing for quick processing of large sets of images for web optimization, dataset creation, or standardizing media assets.

✨ Features
 * Batch Processing: Processes every image file found in the input directory.
 * Custom Dimensions: Easily specify the desired output width and height.
 * Organized Output: Saves all resized images to a separate output folder, leaving original files untouched.
 * Error Handling: Skips files that aren't valid images without crashing the script.

⚙ Prerequisites
To run this script, you need Python and the Pillow (PIL) library installed.
Installation Steps
 * Install Python (if you don't have it).
 * Install Pillow using pip:
   pip install Pillow

🚀 How to Use
1. File Structure Setup
Create the following folder structure in the same directory as your image_resizer.py script:
/
├── image_resizer.py
├── input_images/
│   ├── photo1.jpg
│   └── picture2.png
└── output_resized/ (This folder will be created by the script)

2. Configure the Script
Open image_resizer.py and modify the three configuration variables under the --- Configuration --- section:
# --- Configuration ---
INPUT_DIR = 'input_images'     # The folder containing your original images
OUTPUT_DIR = 'output_resized'  # The folder where the resized images will be saved
TARGET_SIZE = (300, 200)       # The desired size (Width, Height) in pixels

3. Run the Script
Execute the script from your terminal:
python image_resizer.py

4. Check Results
The resized images will appear in the output_resized folder, each saved with a _resized suffix to distinguish them from the originals.

🛠 Technology Stack
 * Language: Python
 * Libraries: Pillow (PIL fork) for image manipulation, os for file system interaction.

📝 Deliverable
A single Python script (image_resizer.py) that successfully reads all image files from a designated input folder, resizes them to the specified dimensions, and saves the new files to a designated output folder.
