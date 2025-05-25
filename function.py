
def get_desktop_path():
    return os.path("Desktop")

def full_path(name):
    return os.path.join(get_desktop_path(), name)

def file_exists(name):
    return os.path.isfile(full_path(name))

def folder_exists(name):
    return os.path.isdir(full_path(name))

def create_txt_file():
    while True:
        name = input("Enter .txt file name (without extension): ")
        if not name:
            print("Filename cannot be empty.")
            continue
        if file_exists(name):
            print("File already exists.")
        else:
            open(full_path(name), "w").close()
            print(f"File '{name}' created on Desktop.")
            break

def read_txt_file():
    name = input("Enter .txt file name to read: ")
    
    if file_exists(name):
        with open(full_path(name), "r") as f:
            content = f.read()
            print("\n===== File Contents =====")
            print(content or "(File is empty)")
    else:
        print("File not found.")

def delete_file():
    name = input("Enter file name to delete (with or without .txt): ")
    path = full_path(name)
    if os.path.isfile(path):
        os.remove(path)
        print(f"File '{name}' deleted.")
    else:
        print("File not found.")

def search_file_or_folder():
    target = input("Enter the name of file or folder to search: ")
    found = False
    for root, dirs, files in os.walk(get_desktop_path()):
        if target in files or target in dirs:
            print("Found at:", os.path.join(root, target))
            found = True
    if not found:
        print("Not found on Desktop.")

def create_folder():
    name = input("Enter folder name to create: ")
    path = full_path(name)
    if os.path.isdir(path):
        print("Folder already exists.")
    else:
        os.makedirs(path)
        print(f"Folder '{name}' created on Desktop.")
