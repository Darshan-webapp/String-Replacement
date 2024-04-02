import os

def replace_in_file(file_path, old_string, new_string):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Perform the replacements
        new_content = file_content.replace(old_string.lower(), new_string.lower())
        new_content = new_content.replace(old_string.upper(), new_string.upper())
        new_content = new_content.replace(old_string.capitalize(), new_string.capitalize())

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)
            
        print(f"Replacement successful in {file_path}!")
        
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

def replace_in_files(directory, old_string, new_string):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                replace_in_file(file_path, old_string, new_string)

# Example usage:
directory = 'C:\\Users\\Acer\\Desktop\\Replace'

old_string = 'Alien'
new_string = 'Birds'

replace_in_files(directory, old_string, new_string)
