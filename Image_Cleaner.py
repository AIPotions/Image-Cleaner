import os
import time
from PIL import Image
import concurrent.futures
import sys

def remove_metadata_from_image(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            # Save image without metadata
            img.save(output_path, quality=95, optimize=True)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_image(image_filename, input_directory, output_directory):
    input_path = os.path.join(input_directory, image_filename)
    output_path = os.path.join(output_directory, image_filename)
    remove_metadata_from_image(input_path, output_path)

def process_images_in_directory(directory):
    output_directory = os.path.join(directory, "cleaned_images")
    os.makedirs(output_directory, exist_ok=True)

    # List all files in the directory
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Measure time for parallel processing
    start_time = time.time()

    print("Starting image processing...")

    # Process images in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_image, image_file, directory, output_directory)
            for image_file in image_files
        ]
        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Write to log file
    log_filename = os.path.join(directory, "Images_are_Ready.txt")
    with open(log_filename, "w") as log_file:
        log_file.write(f"Image processing started at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}\n")
        log_file.write(f"Image processing completed at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}\n")
        log_file.write(f"Total time taken: {elapsed_time:.2f} seconds\n")

    print(f"Processing completed in {elapsed_time:.2f} seconds. Check 'Images_are_Ready.txt' for details.")

if __name__ == "__main__":
    # Check if the script is running from a bundle
    if getattr(sys, 'frozen', False):
        # If running from a bundle (PyInstaller), get the directory of the executable
        current_directory = os.path.dirname(sys.executable)
    else:
        # If running normally, get the directory of the script
        current_directory = os.path.dirname(os.path.abspath(__file__))
    
    process_images_in_directory(current_directory)
