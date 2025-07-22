import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_contents = os.listdir(target_dir)
        files_info = ""

        for obj in dir_contents:
            obj_path = os.path.join(target_dir, obj)
            info_row = f'- {obj}: file_size={os.path.getsize(obj_path)} bytes, is_dir={os.path.isdir(obj_path)}\n'
            files_info += info_row
        
        return files_info
    except Exception as e:
        return f"Error listing files: {e}"
