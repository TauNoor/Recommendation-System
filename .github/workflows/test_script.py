import os
import pandas as pd

# Check current working directory
print(f"Current working directory: {os.getcwd()}")

# List files in the current directory
print(f"Files in the current directory: {os.listdir(os.getcwd())}")

file_name = "movies.csv"
file_name2 = "ratings.csv"

abs_path1 = os.path.abspath(file_name)
abs_path2 = os.path.abspath(file_name2)

print(f"Absolute path for movies.csv: {abs_path1}")
print(f"Absolute path for ratings.csv: {abs_path2}")

# Verify the existence of the files
if os.path.exists(abs_path1) and os.path.exists(abs_path2):
    movies = pd.read_csv(abs_path1)
    users = pd.read_csv(abs_path2)
    print("Files loaded successfully")
else:
    if not os.path.exists(abs_path1):
        print(f"File not found: {abs_path1}")
    if not os.path.exists(abs_path2):
        print(f"File not found: {abs_path2}")
