import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        # Absolute path of working directory
        abs_working_dir = os.path.abspath(working_directory)
        abs_working_dir = os.path.normpath(abs_working_dir)

        # Absolute path of the target file (relative to working directory)
        file_abs_path = os.path.abspath(
            os.path.join(abs_working_dir, file_path))
        file_abs_path = os.path.normpath(file_abs_path)

        # Ensure the file is inside the working directory
        valid_path = os.path.commonpath(
            [abs_working_dir, file_abs_path]) == abs_working_dir
        if not valid_path:
            return f"Error: Cannot read '{file_path}' as it is outside the permitted work directory"

        # Check if the file exists and is a file
        if not os.path.isfile(file_abs_path):
            return f"Error: File not found or is not a regular file: '{file_path}'"

        # Read up to MAX_CHARS from the file
        with open(file_abs_path, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):  # Check if file was larger than MAX_CHARS
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"
