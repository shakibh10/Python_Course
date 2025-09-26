import os

# Function to print directory contents
def print_directory_contents(directory):
    try:
        # List all files and directories
        contents = os.listdir(directory)
        print(f"Contents of {directory}:")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = ".. /"  # Change this to the desired directory path
print_directory_contents(directory_path)
