# Json-Merger

Json-Merger is a simple Python Script that takes multiple JSON scripts and combines them into an array of objects. 

By default, the output is only 500 items per file. Anything beyond that is split among multiple files. 

Example:
```bash
Merged_1.json
Merged_2.json
```

You can change the default value but editing the max_objects_per_file value in the merge_json_files function.
```bash
max_objects_per_file=500
```

## Installation & Usage

1. Clone the repo.
2. Place the JSON files you want to be merged into the "json_files" folder inside the root directory of the project.
3. Run the following command:
```bash
python3 jsonMerger.py
```



