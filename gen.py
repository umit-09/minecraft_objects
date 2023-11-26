import os
import shutil
import json

def copy_and_rename_files(base_path, data, destination_path):
    not_found_files = []  # to store files that were not found

    for key, value in data.items():
        hash_prefix = value["hash"][:2]
        original_path = os.path.join(base_path, hash_prefix, value["hash"])
        new_path = os.path.join(destination_path, key)

        try:
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            shutil.copy(original_path, new_path)
            print(f"Copied: {original_path} -> {new_path}")
        except FileNotFoundError:
            not_found_files.append(original_path)
            print(f"File not found: {original_path}. Skipping.")

    # Print files that were not found
    if not_found_files:
        print("\nFiles not found:")
        for file_path in not_found_files:
            print(file_path)

if __name__ == "__main__":
    # Replace 'your_json_file.json' with the actual path to your JSON file
    json_file_path = '10.json'

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Replace 'your_base_path' with the actual base directory where your files are located
    base_path = 'objects'
    
    # Replace 'renamed_objs' with the desired name for the new directory
    destination_path = 'renamed_objs'

    copy_and_rename_files(base_path, data["objects"], destination_path)
