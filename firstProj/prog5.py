# write a python script to delete older files from nexus artifact to clear space.

import os
import shutil

def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file '{file_path}': {e}")
    else:
        print(f"File '{file_path}' does not exist.")


def delete_directory(dir_path):
    if os.path.exists(dir_path):
        try:
            shutil.rmtree(dir_path)
            print(f"Directory '{dir_path}' and its contents deleted successfully.")
        except Exception as e:
            print(f"Error deleting directory '{dir_path}': {e}")
    else:
        print(f"Directory '{dir_path}' does not exist.")


if __name__ == "__main__":
    file_path_to_delete = "example.txt"
    dir_path_to_delete = "example_dir"

    # Create dummy file and directory for testing
    with open(file_path_to_delete, "w") as f:
        f.write("This is a test file.")
    os.makedirs(dir_path_to_delete, exist_ok=True)
    with open(os.path.join(dir_path_to_delete, "another_file.txt"), "w") as f:
        f.write("This is another test file.")

    delete_file(file_path_to_delete)
    delete_directory(dir_path_to_delete)