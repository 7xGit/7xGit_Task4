import os

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

def normalize_txt_name(name):
    name = name.strip()
    if not name.endswith(".txt"):
        name += ".txt"
    return name

def full_path(name):
    return os.path.join(get_desktop_path(), name)

def file_exists(name):
    return os.path.isfile(full_path(normalize_txt_name(name)))

def folder_exists(name):
    return os.path.isdir(full_path(name.strip()))

def create_txt_file():
    while True:
        name = input("Enter .txt file name (without extension): ").strip()
        if not name:
            print("Filename cannot be empty.")
            continue
        name = normalize_txt_name(name)
        if file_exists(name):
            print("File already exists.")
        else:
            with open(full_path(name), "w") as f:
                pass
            print(f"File '{name}' created on Desktop.")
            break

def read_txt_file():
    name = input("Enter .txt file name to read: ")
    name = normalize_txt_name(name)
    if file_exists(name):
        with open(full_path(name), "r") as f:
            content = f.read()
            print("\n===== File Contents =====")
            print(content if content else "(File is empty)")
    else:
        print("File not found.")

def delete_file():
    name = input("Enter file name to delete (with or without .txt): ")
    name = normalize_txt_name(name)
    path = full_path(name)
    if os.path.isfile(path):
        os.remove(path)
        print(f"File '{name}' deleted.")
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
