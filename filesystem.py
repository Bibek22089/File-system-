import os

# Create a new file in a chosen directory
def create_file():
    directory = input("Enter the directory path to create the file: ")
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    filename = input("Enter the file name to create: ")
    full_path = os.path.join(directory, filename)
    try:
        with open(full_path, 'w') as file:
            pass
        print(f"File {full_path} has been created.")
    except PermissionError:
        print("Permission denied. Unable to create the file.")
    except FileNotFoundError:
        print("Invalid file name or path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Read the contents of a file
def read_file():
    directory = input("Enter the directory path to list files: ")
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    try:
        files = os.listdir(directory)
        if len(files) > 0:
            print(f"Files in directory {directory}:")
            for i, file in enumerate(files):
                full_path = os.path.join(directory, file)
                print(f"{i+1}. {full_path}, {os.path.getsize(full_path)} bytes")
            
            choice = input("Enter the number of the file to read: ")
            try:
                index = int(choice) - 1
                if index >= 0 and index < len(files):
                    filename = os.path.join(directory, files[index])
                    try:
                        with open(filename, 'r') as file:
                            contents = file.read()
                            if contents:
                                print(contents)
                            else:
                                print("The file is empty.")
                    except PermissionError:
                        print("Permission denied. Unable to read the file.")
                    except FileNotFoundError:
                        print(f"File {filename} does not exist.")
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"No files found in directory {directory}.")
    except PermissionError:
        print("Permission denied. Unable to list files in the directory.")

# Write data to a file
def write_file():
    directory = input("Enter the directory path to list files: ")
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    try:
        files = os.listdir(directory)
        if len(files) > 0:
            print(f"Files in directory {directory}:")
            for i, file in enumerate(files):
                full_path = os.path.join(directory, file)
                print(f"{i+1}. {full_path}, {os.path.getsize(full_path)} bytes")
            
            choice = input("Enter the number of the file to write to: ")
            try:
                index = int(choice) - 1
                if index >= 0 and index < len(files):
                    filename = os.path.join(directory, files[index])
                    data = input("Enter the data to write: ")
                    try:
                        with open(filename, 'a') as file:
                            file.write(data)
                            print("Data has been written to the file.")
                    except PermissionError:
                        print("Permission denied. Unable to write to the file.")
                    except FileNotFoundError:
                        print(f"File {filename} does not exist.")
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"No files found in directory {directory}.")
    except PermissionError:
        print("Permission denied. Unable to list files in the directory.")

# Rename a file
def rename_file():
    directory = input("Enter the directory path to list files: ")
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    try:
        files = os.listdir(directory)
        if len(files) > 0:
            print(f"Files in directory {directory}:")
            for i, file in enumerate(files):
                full_path = os.path.join(directory, file)
                print(f"{i+1}. {full_path}, {os.path.getsize(full_path)} bytes")
            
            choice = input("Enter the number of the file to rename: ")
            try:
                index = int(choice) - 1
                if index >= 0 and index < len(files):
                    old_name = os.path.join(directory, files[index])
                    new_name = input("Enter the new name: ")
                    new_path = os.path.join(directory, new_name)
                    try:
                        os.rename(old_name, new_path)
                        print(f"{old_name} has been renamed to {new_path}.")
                    except PermissionError:
                        print("Permission denied. Unable to rename the file.")
                    except FileNotFoundError:
                        print(f"File {old_name} does not exist.")
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"No files found in directory {directory}.")
    except PermissionError:
        print("Permission denied. Unable to list files in the directory.")


# Change file permission
def change_permission():
    filename = input("Enter the file name to change permission: ")
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    # Prompt for new permission
    while True:
        new_permission = input("Enter the new permission value for the user (0-7): ")
        if not new_permission.isdigit() or int(new_permission) < 0 or int(new_permission) > 7:
            print("Invalid permission value. Please enter a value between 0 and 7.")
        else:
            break

    # Calculate the new permission value
    permission = int(new_permission, 8)

    try:
        os.chmod(filename, permission)
        print(f"Permission of file {filename} has been changed to {permission:o}.")
    except ValueError:
        print("Invalid permission values. Permission not changed.")
    except PermissionError:
        print("Permission denied. Unable to change permission.")
    except FileNotFoundError:
        print(f"File {filename} does not exist.")

# Set permissions for a file
def set_permission():
    filename = input("Enter the file path: ")
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return

    try:
        current_mode = oct(os.stat(filename).st_mode)[-3:]
        print(f"Current permission mode for {filename}: {current_mode}")

        # Ask the user for the new permission mode
        new_mode = input("Enter the new permission mode (e.g. 777, 742, 000): ")
        try:
            # Convert the new permission mode to an integer
            new_mode = int(new_mode, 8)

            # Set the new permission mode for the file
            os.chmod(filename, new_mode)
            print(f"Permission mode for {filename} has been set to {oct(new_mode)[-3:]}.")
        except ValueError:
            print("Invalid input. Please enter a valid permission mode.")
        except PermissionError:
            print("Permission denied. Unable to set permissions for the file.")
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
    except PermissionError:
        print("Permission denied. Unable to access file information.")
    except FileNotFoundError:
        print(f"File {filename} does not exist.")

# Delete a file
def delete_file():
    directory = input("Enter the directory path to list files: ")
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    try:
        files = os.listdir(directory)
        if len(files) > 0:
            print(f"Files in directory {directory}:")
            for i, file in enumerate(files):
                full_path = os.path.join(directory, file)
                print(f"{i+1}. {full_path}, {os.path.getsize(full_path)} bytes")
            
            choice = input("Enter the number of the file to delete: ")
            try:
                index = int(choice) - 1
                if index >= 0 and index < len(files):
                    filename = os.path.join(directory, files[index])
                    confirm = input(f"Are you sure you want to delete {filename}? (y/n): ")
                    if confirm.lower() == 'y':
                        try:
                            os.remove(filename)
                            print(f"{filename} has been deleted.")
                        except PermissionError:
                            print("Permission denied. Unable to delete the file.")
                    else:
                        print("Deletion has been cancelled.")
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"No files found in directory {directory}.")
    except PermissionError:
        print("Permission denied. Unable to list files in the directory.")
    except FileNotFoundError:
        print(f"Directory {directory} does not exist.")

# List files in a directory
def list_files():
    directory = input("Enter the directory path to list files: ")
    if os.path.exists(directory):
        try:
            files = os.listdir(directory)
            if len(files) > 0:
                print(f"Files in directory {directory}:")
                for file in files:
                    full_path = os.path.join(directory, file)
                    print(f"{full_path}, {os.path.getsize(full_path)} bytes")
            else:
                print(f"No files found in directory {directory}.")
        except PermissionError:
            print("Permission denied. Unable to list files in the directory.")
        except FileNotFoundError:
            print(f"Directory {directory} does not exist.")
    else:
        print(f"Directory {directory} does not exist.")

# Test the file system functions
def test_file_system():
    while True:
        print("Choose an option:")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Write to a file")
        print("4. Rename a file")
        print("5. Change file permission")
        print("6. Delete a file")
        print("7. List files in a directory")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            write_file()
        elif choice == "4":
            rename_file()
        elif choice == "5":
            change_permission()
        elif choice == "6":
            delete_file()
        elif choice == "7":
            list_files()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the test
test_file_system()
