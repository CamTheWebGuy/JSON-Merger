import os
import json

def merge_json_files(folder_path, output_file_prefix, max_objects_per_file=500):
    merged_data = []
    file_counter = 1
    object_counter = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                merged_data.append(data)
                object_counter += 1

                if object_counter >= max_objects_per_file:
                    output_file_name = f"{output_file_prefix}_{file_counter}.json"
                    output_data = json.dumps(merged_data)

                    output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file_name)

                    with open(output_file_path, "w") as output_file:
                        output_file.write(output_data)

                    merged_data = []
                    file_counter += 1
                    object_counter = 0

    # Save any remaining data to the last file
    if merged_data:
        output_file_name = f"{output_file_prefix}_{file_counter}.json"
        output_data = json.dumps(merged_data)

        output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file_name)

        with open(output_file_path, "w") as output_file:
            output_file.write(output_data)

if __name__ == "__main__":
    json_files_folder = "json_files"  # Replace this with the path to your folder containing JSON files
    output_file_prefix = "merged_file"
    
    merge_json_files(json_files_folder, output_file_prefix)
    print("JSON files merged successfully.")
