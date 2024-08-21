import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image

def get_current_directory():
    """Return the directory where the script or executable is located."""
    if getattr(sys, 'frozen', False):
        # Running from a bundle (PyInstaller)
        return os.path.dirname(sys.executable)
    else:
        # Running as a script
        return os.path.dirname(os.path.abspath(__file__))

def remove_pnginfo_metadata(input_image_path, output_image_path):
    try:
        with Image.open(input_image_path) as img:
            if img.mode != 'RGBA':
                img = img.convert('RGBA')  # Convert image to RGBA if it's not already
            
            r, g, b, a = img.split()
            rgb_img = Image.merge('RGB', (r, g, b))
            rgb_img.save(output_image_path, format='PNG')
        return f"Processed {input_image_path}"
    except Exception as e:
        return f"Error processing {input_image_path}: {e}"

def process_images_in_directory(directory):
    output_directory = os.path.join(directory, 'processed_images')
    os.makedirs(output_directory, exist_ok=True)

    png_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]
    input_image_paths = [os.path.join(directory, f) for f in png_files]
    output_image_paths = [os.path.join(output_directory, f) for f in png_files]

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(remove_pnginfo_metadata, input_path, output_path): input_path
            for input_path, output_path in zip(input_image_paths, output_image_paths)
        }

        for future in as_completed(futures):
            result = future.result()
            print(result)

    end_time = time.time()
    elapsed_time = end_time - start_time

    log_filename = os.path.join(directory, "Your_Images_Are_Ready.txt")
    with open(log_filename, "w") as log_file:
        log_file.write(f"Processing started at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}\n")
        log_file.write(f"Processing completed at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}\n")
        log_file.write(f"Total time taken: {elapsed_time:.2f} seconds\n")

    print(f"Processing completed in {elapsed_time:.2f} seconds. Check 'Your_Images_Are_Ready.txt' for details.")

if __name__ == "__main__":
    current_directory = get_current_directory()
    process_images_in_directory(current_directory)
