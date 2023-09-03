import os
import glob

# Get the current working directory
current_path = os.getcwd()

# Define the file extension you want to delete (in this case, .csv)
file_extension = ".csv"

# Create a glob pattern to match files with the specified extension
pattern = f"*{file_extension}"

# Use glob to find files matching the pattern in the current directory
csv_files = glob.glob(os.path.join(current_path, pattern))

# Loop through the matching files and delete them
for csv_file in csv_files:
    try:
        os.remove(csv_file)
        print(f"Deleted: {csv_file}")
    except Exception as e:
        print(f"Failed to delete {csv_file}: {e}")
