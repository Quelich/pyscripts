import os


def capitalize_filenames(directory):
    for filename in os.listdir(directory):
        # Ignore directories and files starting with uppercase letters
        if not filename.startswith('.') and not filename[0].isupper():
            # Get the old and new filenames
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, filename.capitalize())

            # Rename the file
            os.rename(old_path, new_path)


# Example usage
capitalize_filenames(
    'C:\\Users\\emre1\\OneDrive\\Masaüstü\\flags\\europe\\circle')
