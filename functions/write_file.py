import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        working_dir_abs_path = os.path.normpath(working_directory)

        file_path_abs = os.path.abspath(
            os.path.join(working_dir_abs_path, file_path))
        file_path_abs = os.path.normpath(file_path_abs)

        valid_path = os.path.commonpath([working_dir_abs_path, file_path_abs]) == working_dir_abs_path
        if not valid_path:
            return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory."
        
        if os.path.isdir(file_path_abs):
            return f"Error: cannot write to '{file_path}' as it is a directory"

        parent_dir = os.path.dirname(file_path_abs)
        os.makedirs(parent_dir, exist_ok=True)

        with open(file_path_abs, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"

    except Exception as e:
        return f"Error: {str(e)}"
