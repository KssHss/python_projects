import pandas as pd 
import os 
from os import system
import pandas as pd
import matplotlib.pyplot as plt

folder = "/Users/hassania/Downloads/"  # Replace with the actual path to the folder
file = "Solubility.csv"              # Replace with the actual filename if different

path = os.path.join(folder, file)
path = os.path.abspath(path)

# Print the path to verify if it's correct
print(f"Looking for file at: {path}") 

# Try to open the file to check for permissions
try:
    with open(path, 'r') as f:
        pass  # If the file opens successfully, do nothing
except FileNotFoundError:
    print(f"Error: File not found at {path}. Please check the file name and path.")
except PermissionError:
    print(f"Error: Permission denied to access {path}. Please check your file permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # If no errors occurred, proceed to read the file
    df = pd.read_csv(path, sep=',', decimal='.')
    print(df)  # Print the DataFrame to confirm it loaded correctly