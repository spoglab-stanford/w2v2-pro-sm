import pandas as pd
import json
import os

# this is just a template; it expects a csv with the columns audio_file and label
    # audio_file is the column containing the path for each audio file and label is the column containing the label for each audio file

# Input CSV file paths
csv_files = {
    "train": "Train.csv",
    "dev": "Dev.csv",
    "test": "Test.csv"
}

# Output JSON directory
output_folder = "/path/json_files"

# Path prefixes to add
# you can also not do this and just add the prefix in the hparam
train_dev_prefix = ""
test_prefix = ""

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each CSV file
for split, csv_path in csv_files.items():
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Ensure required columns exist
    required_columns = ["audio_file", "label"]
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Missing required columns in {csv_path}. Expected columns: {required_columns}")

    # Rename columns to match the desired JSON format
    df = df.rename(columns={
        "audio_file": "wav",
        "label": "label"
    })

    # Prepend the appropriate prefix to the 'wav' column
    if split in ["train", "dev"]:
        df["wav"] = df["wav"].apply(lambda x: f"{train_dev_prefix}/{x}")
    else:
        df["wav"] = df["wav"].apply(lambda x: f"{test_prefix}{x}")

    # Extract the file name (without extension) as the key
    df["key"] = df["wav"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Convert the DataFrame to a dictionary with file names as keys
    data = {
        row.key: {
            "wav": row.wav,
            "label": row.label
        }
        for row in df.itertuples()
    }

    # Save to JSON
    # output_json_path = os.path.join(output_folder, f"{split}_bc.json")
    output_json_path = os.path.join(output_folder, f"{split}.json")
    with open(output_json_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"{split.capitalize()} JSON saved to: {output_json_path}")
