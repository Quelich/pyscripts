import os


def remove_underscore(directory):
    for filename in os.listdir(directory):
        # Ignore directories and files without an underscore in their names
        if not filename.startswith('.') and '_' in filename:
            # Get the old and new filenames
            old_path = os.path.join(directory, filename)
            new_filename = filename.replace('_', ' ')
            new_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_path, new_path)


# Example usage
remove_underscore(
    'C:\\Users\\emre1\\OneDrive\\Masaüstü\\flags\\europe\\circle')
