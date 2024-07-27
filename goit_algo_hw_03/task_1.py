import os
import shutil
import sys

def get_file_extension(filename):
    _, ext = os.path.splitext(filename)
    return ext[1:] if ext else 'no_extension'

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def copy_file(source_path, dest_path):
    try:
        shutil.copy2(source_path, dest_path)
        print(f"Сoping {source_path} -> {dest_path}")
    except Exception as e:
        print(f"The error while coping {source_path}: {e}")

def process_item(source_path, destination_dir):
    if os.path.isdir(source_path):
        copy_files_recursive(source_path, destination_dir)
    else:
        ext = get_file_extension(source_path)
        dest_subdir = os.path.join(destination_dir, ext)
        create_directory(dest_subdir)
        dest_path = os.path.join(dest_subdir, os.path.basename(source_path))
        copy_file(source_path, dest_path)

def copy_files_recursive(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            process_item(source_path, destination_dir)
    except Exception as e:
        print(f"The error while processing the dir {source_dir}: {e}")

def parse_arguments():
    if len(sys.argv) < 2:
        print("THe pathing to the source directory is required.")
        print("Usage: python sendbox.py <source_dir> [destination_dir]")
        sys.exit(1)

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(source_dir):
        print(f"The source directory {source_dir} does not exist.")
        sys.exit(1)

    return source_dir, destination_dir

def main():
    source_dir, destination_dir = parse_arguments()
    copy_files_recursive(source_dir, destination_dir)

if __name__ == "__main__":
    main()