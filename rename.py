import os

# Set the path to your directory
directory = "/home/luisdogo/Desktop/EDA/HUPA-UCM Diabetes Dataset/Preprocessed"

# List all CSV files in the directory
csv_files = sorted([f for f in os.listdir(directory) if f.lower().endswith('.csv')])

# Sort to make sure order is consistent (you can sort by created time, name, etc.)
csv_files.sort()

# Rename each file
for i, filename in enumerate(csv_files, start=1):
    old_path = os.path.join(directory, filename)
    new_name = f"HUPA{i:04}.csv"
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")
