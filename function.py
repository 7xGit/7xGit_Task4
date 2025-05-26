class Node:
    def __init__(self, name, parent=None, is_dir=True):
        self.name = name
        self.is_dir = is_dir
        self.children = {}  # name -> Node
        self.parent = parent

class FileSystem:
    def __init__(self):
        self.root = Node("root")
        self.current = self.root

    def mkdir(self, name):
        if name in self.current.children:
            print(f"Directory '{name}' already exists.")
        else:
            self.current.children[name] = Node(name, parent=self.current)
            print(f"Directory '{name}' created.")

    def ls(self):
        if not self.current.children:
            print("(empty)")
        else:
            for child in self.current.children.values():
                print(f"{child.name}/" if child.is_dir else child.name)

    def cd(self, name):
        if name == "..":
            if self.current.parent:
                self.current = self.current.parent
            else:
                print("Already at root.")
        elif name in self.current.children and self.current.children[name].is_dir:
            self.current = self.current.children[name]
        else:
            print(f"No such directory: {name}")

    def pwd(self):
        path = []
        node = self.current
        while node:
            path.append(node.name)
            node = node.parent
        print("/" + "/".join(reversed(path[:-1])))

    def rm(self, name):
        if name not in self.current.children:
            print(f"No such directory: {name}")
        elif not self.current.children[name].is_dir:
            print(f"{name} is not a directory.")
        else:
            del self.current.children[name]
            print(f"Directory '{name}' removed.")
