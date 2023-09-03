import os
import glob

# Get the current working directory
current_path = os.getcwd()

# Define the file extension you want to check (in this case, .csv)
file_extension = ".csv"

# Create a glob pattern to match files with the specified extension
pattern = f"*{file_extension}"

# Use glob to find files matching the pattern in the current directory
csv_files = glob.glob(os.path.join(current_path, pattern))

# Check if any .csv files were found
if csv_files:
    print("Found .csv files:")
    for csv_file in csv_files:
        print(csv_file)
else:
    print("No .csv files found in the current directory.")
