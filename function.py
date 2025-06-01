import os

# def get_desktop_path():
#     return os.path("Desktop")

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

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

def menu():
    while True:
        print("\n==== Desktop File Manager ====")
        print("1. Create new .txt file")
        print("2. Read a .txt file")
        print("3. Delete a .txt file")
        print("4. Search for a file/folder on Desktop")
        print("5. Create new folder on Desktop")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            create_txt_file()
        elif choice == '2':
            read_txt_file()
        elif choice == '3':
            delete_file()
        elif choice == '4':
            search_file_or_folder()
        elif choice == '5':
            create_folder()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    menu()
    