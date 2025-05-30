import os

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

def add_txt_extension(name):
    return name if name.endswith(".txt") else name + ".txt"

def full_path(name):
    return os.path.join(get_desktop_path(), name)

def file_exists(name):
    return os.path.isfile(full_path(add_txt_extension(name)))


def folder_exists(name):
    return os.path.isdir(full_path(name))

# Create a new .txt file
def create_txt_file():
    while True:
        name = input("Enter .txt file name (without extension): ").strip()
        if not name:
            print("Filename cannot be empty.")
            continue

        name = add_txt_extension(name)

        if file_exists(name):
            print(f"File '{name}' already exists on Desktop.")
        else:
            try:
                with open(full_path(name), "w") as f:
                    pass
                print(f"File '{name}' created on Desktop.")
            except Exception as e:
                print("Error creating file:", e)
            break

# Read a .txt file
def read_txt_file():
    name = input("Enter .txt file name to read: ").strip()
    name = add_txt_extension(name)

    if file_exists(name):
        try:
            with open(full_path(name), "r") as f:
                content = f.read()
                print("\n===== File Contents =====")
                print(content if content else "(File is empty)")
        except Exception as e:
            print("Error reading file:", e)
    else:
        print(f"File '{name}' not found on Desktop.")

# Delete a .txt file
def delete_file():
    name = input("Enter file name to delete (with or without .txt): ").strip()
    name = add_txt_extension(name)
    path = full_path(name)

    if os.path.isfile(path):
        try:
            os.remove(path)
            print(f"File '{name}' deleted.")
        except Exception as e:
            print("Error deleting file:", e)
    else:
        print(f"File '{name}' not found on Desktop.")

# Search for a file or folder on Desktop
def search_file_or_folder():
    target = input("Enter the name of file or folder to search: ").strip()
    found = False
    for root, dirs, files in os.walk(get_desktop_path()):
        if target in files or target in dirs:
            print("Found at:", os.path.join(root, target))
            found = True
    if not found:
        print(f"'{target}' not found on Desktop.")

# Create a new folder on Desktop
def create_folder():
    name = input("Enter folder name to create: ").strip()
    if not name:
        print("Folder name cannot be empty.")
        return

    path = full_path(name)

    if os.path.isdir(path):
        print(f"Folder '{name}' already exists on Desktop.")
    else:
        try:
            os.makedirs(path)
            print(f"Folder '{name}' created on Desktop.")
        except Exception as e:
            print("Error creating folder:", e)
