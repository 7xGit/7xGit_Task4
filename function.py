import os

def get_desktop_path():
    path = os.path.join(os.path.expanduser("~"), "Desktop")
    # Ensure the Desktop folder exists (create if not)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def full_path(name):
    return os.path.join(get_desktop_path(), name)

def file_exists(name):
    return os.path.isfile(full_path(name))

def folder_exists(name):
    return os.path.isdir(full_path(name))

def create_txt_file():
    while True:
        name = input("Enter .txt file name (without extension): ").strip()
        if not name:
            print("Filename cannot be empty.")
            continue
        full_name = name if name.endswith(".txt") else name + ".txt"
        if file_exists(full_name):
            print("File already exists.")
        else:
            open(full_path(full_name), "w").close()
            print(f"File '{full_name}' created on Desktop.")
            break

def read_txt_file():
    name = input("Enter .txt file name to read: ").strip()
    full_name = name if name.endswith(".txt") else name + ".txt"
    if file_exists(full_name):
        with open(full_path(full_name), "r") as f:
            content = f.read()
            print("\n===== File Contents =====")
            print(content or "(File is empty)")
    else:
        print("File not found.")

def delete_file():
    name = input("Enter file name to delete (with or without .txt): ").strip()
    full_name = name if name.endswith(".txt") else name + ".txt"
    path = full_path(full_name)
    if os.path.isfile(path):
        os.remove(path)
        print(f"File '{full_name}' deleted.")
    else:
        print("File not found.")

def search_file_or_folder():
    target = input("Enter the name of file or folder to search: ").strip()
    found = False
    for root, dirs, files in os.walk(get_desktop_path()):
        if target in files or target in dirs:
            print("Found at:", os.path.join(root, target))
            found = True
    if not found:
        print("Not found on Desktop.")

def create_folder():
    name = input("Enter folder name to create: ").strip()
    path = full_path(name)
    if os.path.isdir(path):
        print("Folder already exists.")
    else:
        os.makedirs(path)
        print(f"Folder '{name}' created on Desktop.")
