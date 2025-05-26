from function import FileSystem

def main():
    fs = FileSystem()
    print("Welcome to the File Manager Simulator!")
    print("Type commands like: mkdir, ls, cd, pwd, rm, exit")

    while True:
        command = input("> ").strip()
        if not command:
            continue

        parts = command.split()
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        if cmd == "mkdir":
            if arg:
                fs.mkdir(arg)
            else:
                print("Usage: mkdir <dirname>")
        elif cmd == "ls":
            fs.ls()
        elif cmd == "cd":
            if arg:
                fs.cd(arg)
            else:
                print("Usage: cd <dirname>")
        elif cmd == "pwd":
            fs.pwd()
        elif cmd == "rm":
            if arg:
                fs.rm(arg)
            else:
                print("Usage: rm <dirname>")
        elif cmd == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command:", cmd)

if __name__ == "__main__":
    main()
