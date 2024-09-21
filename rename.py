import os
import re

def sanitize_filename(filename):
    sanitized = re.sub(r'[^a-zA-Z0-9_]+', '_', filename)
    sanitized = sanitized.strip('_')
    return sanitized

def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            name, ext = os.path.splitext(file_name)
            original_file_path = os.path.join(root, file_name)

            new_name = sanitize_filename(name)
            new_name = re.sub(r'_+', '_', new_name)
            new_file_name = new_name + ext
            new_file_path = os.path.join(root, new_file_name)

            if original_file_path != new_file_path:
                print(f'Renaming: "{original_file_path}" to "{new_file_path}"')
                os.rename(original_file_path, new_file_path)

if __name__ == "__main__":
    current_directory = os.getcwd()
    rename_files_in_directory(current_directory)
