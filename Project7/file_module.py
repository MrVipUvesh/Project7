import os

class FileHandling:
    def create_file(self, name):
        if(name == ""):
            print("[Error: File name can't be empty!]")
            return
        else:
            try:
                with open(name, "x") as file:
                    file.close()
                    print("File created successfully!")
            except FileExistsError:
                print("[Error: File already exist!]")
                return

    def write_file(self, name, text):
        if(name == ""):
            print("[Error: Fine name can't be empty]")
            return
        else:
            try:
                with open(name, "w") as file:
                    file.write(text)
                    print("Text added successfully!")
            except FileNotFoundError:
                print(f"[Error: File named {name} does not exist!]")
                return

    def read_file(self, name):
        if(name == ""):
            print("[Error: File name can't be empty]")
        else:
            try:
                with open(name, "r") as file:
                    text = file.readlines()
                    print(text)
            except FileNotFoundError:
                print(f"[Error: File named {name} does not exist!]")
                return

    def append_file(self, name, text):
        if(name == ""):
            print("[Error: File name can't be empty]")
        else:
            try:
                with open(name, "a") as file:
                    file.write(text)
                    print("Text added successfully!")
            except FileNotFoundError:
                print(f"[Error: File named {name} does not exist!]")
                return

    def del_file(self, name):
        if(name == ""):
            print("[Error: File name can't be empty]")
        else:
            try:
                os.remove(name)
            except FileNotFoundError:
                print(f"[Error: File named {name} does not exist!]")