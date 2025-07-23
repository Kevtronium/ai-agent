import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if os.path.splitext(abs_file_path)[1] != ".py":
        return f'Error: "{file_path} is not a Python file.'
    
    try:
        process_args = ["python", abs_file_path]
        if len(args) != 0:
            process_args.extend(args)
        

        completed_process = subprocess.run(process_args, cwd=abs_working_dir, timeout=30, capture_output=True, text=True)

        output = []
        if completed_process.stdout:
            output.append(f'STDOUT:\n{completed_process.stdout}')
        if completed_process.stderr:
            output.append(f'STDERR:\n{completed_process.stderr}')
        if completed_process.returncode != 0:
            output.append()
            return f"Process exited with code {completed_process.returncode}"
    
        return "\n".join(output) if output else "No output produced."
    
    except Exception as e:
        return f"Error: executing Python file: {e}"


