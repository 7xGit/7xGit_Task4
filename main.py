import os

from function import create_txt_file, read_txt_file, delete_file, search_file_or_folder, create_folder

def menu():
    while True:
        print("\n===== Desktop File Manager =====")
        print("1. Create new .txt file")
        print("2. Read a .txt file")
        print("3. Delete a .txt file")
        print("4. Search for a file/folder on Desktop")
        print("5. Create new folder on Desktop")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ")

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
