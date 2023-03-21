

# todo
# 1. step
# get source directory as parameter in a different method
# count each file in the source directory in a different method
# print file names in the source directory in a different method
# count files in the source directory in a different method
# print sizes of each file in the source directory in a different method
# count total size of files in the source directory in a different method

import os


def count_files(directory):
    count = 0
    for filename in os.listdir(directory):
        if not filename.startswith('.'):
            count += 1
    return count


def print_files(directory):
    for filename in os.listdir(directory):
        if not filename.startswith('.'):
            path = os.path.join(directory, filename)
            size = os.path.getsize(path)
            print(f"{filename}: {size} bytes")


def count_total_size(directory):
    total_size = 0
    for filename in os.listdir(directory):
        if not filename.startswith('.'):
            path = os.path.join(directory, filename)
            size = os.path.getsize(path)
            total_size += size
    return total_size


def convert_bytes_to_megabytes(bytes_val):
    megabytes = bytes_val / 1024 / 1024
    return megabytes


def convert_bytes_to_gigabytes(bytes_val):
    gigabytes = bytes_val / 1024 / 1024 / 1024
    return gigabytes


if __name__ == '__main__':
    directory = "C:\\Users\\emre1\\OneDrive\\Masaüstü\\flags\\all\\circle"
    print(f"Number of files in {directory}: {count_files(directory)}")
    print(f"Files in {directory}:")
    print_files(directory)

    bytes_val = count_total_size(directory)
    megabytes_val = convert_bytes_to_megabytes(bytes_val)
    gigabytes_val = convert_bytes_to_gigabytes(bytes_val)
    print(
        f"Total size of files in {directory}:\n\t {bytes_val:} bytes ({megabytes_val:.2f} MB, {gigabytes_val:.2f} GB)")


# 2. step
# make a new destination directory of pixel size, e.g., 100x100
# change the size of images (.png, .jpg, .jpeg) to, e.g., 100x100
# save the image to the new directory
