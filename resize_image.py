import os
from PIL import Image


def resize_images(src_dir, new_dir, new_size):
    # Create a new directory inside the source directory with the name of the new size
    new_dir_path = os.path.join(src_dir, new_dir)
    os.makedirs(new_dir_path, exist_ok=True)

    # Loop through all the files in the source directory
    for file_name in os.listdir(src_dir):
        # Check if the file is an image file
        if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):
            # Open the image file using PIL
            img_path = os.path.join(src_dir, file_name)
            img = Image.open(img_path)

            # Resize the image to the new size
            new_img = img.resize(new_size)

            # Save the resized image to the new directory with the same filename
            new_img_path = os.path.join(new_dir_path, file_name)
            new_img.save(new_img_path)


if __name__ == "__main__":
    src_dir = "C:\\Users\\emre1\\OneDrive\\Masaüstü\\flags\\all\\circle"
    new_dir = "100x100"
    new_size = (100, 100)

    resize_images(src_dir, new_dir, new_size)
