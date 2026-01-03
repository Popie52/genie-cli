import os

def get_files_info(working_directory, directory="."):

    try:
        # get the absolute path first
        abs_path = os.path.abspath(working_directory)

        # try to normalize the path
        target_dir = os.path.normpath(os.path.join(abs_path, directory))

        # check path now
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

        if not valid_target_dir:
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

        if not os.path.isdir(target_dir):
            return f"The directory '{directory}' is not a directory"

        entries = os.listdir(target_dir)
        if not entries:
            return f'The directory "{directory}" is empty.'

        result_lines = []
        for entry in entries:
            entry_path = os.path.join(target_dir, entry)
            is_dir = os.path.isdir(entry_path)
            file_size = os.path.getsize(entry_path) if not is_dir else 0
            result_lines.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(result_lines)
    except Exception as e:
        return f"Error: {str(e)}"