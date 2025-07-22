import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_filepath.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_filepath, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
