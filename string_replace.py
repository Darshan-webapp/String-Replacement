def replace_in_file(file_path, old_string, new_string):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Perform the replacement
        new_content = file_content.replace(old_string, new_string)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)
            
        print("Replacement successful!")
        
    except Exception as e:
        print("An error occurred:", e)

file_path = 'C:\\Users\\Acer\\Desktop\\testing1.txt'
old_string = 'pizza'
new_string = 'burger'

replace_in_file(file_path, old_string, new_string)
